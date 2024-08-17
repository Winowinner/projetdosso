from django.db import models

class Pret_banques(models.Model):
    nom_complet = models.CharField(max_length=200)  
    email = models.CharField(max_length=200)  
    phone = models.CharField(max_length=200)  
    montant_pret = models.CharField(max_length=200)  
    dure_pret = models.CharField(max_length=200)
    message = models.TextField()  
    date_inscription = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nom_complet  # ou tout autre champ représentatif
