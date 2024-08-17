from django.urls import path
from pret.views import index, service, about, FAQ, pret, contact, succes


urlpatterns = [
    path('', index, name="index"),
    path('service/', service, name="service"),
    path('info/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('pret/', pret, name="pret"),
    path('faq/', FAQ, name="FAQ"),
    path('succes/', succes, name="succes"),
]