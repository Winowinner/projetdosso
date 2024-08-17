import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

def send_email_with_html_body(subject: str, receivers: list, template: str, context: dict):
    try: 
        message = render_to_string(template, context)

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            receivers,  # Liste des destinataires
            fail_silently=True,
            html_message=message
        )
        
        return True
    except Exception as e:
        logger.error(e)  # Correction pour logger.error
    return False
