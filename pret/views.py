from django.shortcuts import render, redirect
from datetime import datetime
from .models import Pret_banques
from .utils import send_email_with_html_body  # Assurez-vous que cette fonction est correctement définie
from django.utils.translation import gettext as _

def index(request):
    var = _("welcome")
    return render(request, 'pret/index.html')

def service(request):
    return render(request, 'pret/service.html')

def about(request):
    return render(request, 'pret/about.html')

def FAQ(request):
    return render(request, 'pret/FAQ.html')

def contact(request):
    return render(request, 'pret/contact.html')

def succes(request):
    return render(request, 'pret/testimonial.html')

def form(request):
    return render(request, 'pret/form.html')

def pret(request):
    if request.method == 'POST':
        nom_complet = request.POST.get('nom_complet')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        montant_pret = request.POST.get('montant_pret')
        dure_pret = request.POST.get('dure_pret')
        message = request.POST.get('message')
        code_pays = request.POST.get('code_pays')  # Récupérer le code pays sélectionné

        numero_telephone = f"{code_pays}{phone}"

        # Créer et enregistrer une nouvelle instance du modèle Pret
        nouveau_pret = Pret_banques(
            nom_complet=nom_complet,
            email=email,
            phone=numero_telephone,  # Utiliser le numéro de téléphone complet
            montant_pret=montant_pret,
            dure_pret=dure_pret,
            message=message
        )
        nouveau_pret.save()

        subject = 'Confirmation de votre demande de prêt'
        template = 'pret/email.html'
        context = {
            'date': datetime.today().date(),
            'email': email,
            'nom': nom_complet
        }

        receivers = [email]
        has_send = send_email_with_html_body(subject=subject, receivers=receivers, template=template, context=context)

        if has_send:
            return redirect('../../succes')
        else:
            return render(request, 'pret/pret.html', {"error": "Erreur lors de l'envoi de l'email."})

    return render(request, 'pret/pret.html')
