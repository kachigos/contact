from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact
from django.dispatch import receiver
from django.db.models.signals import post_save
from .send_email import send_contact


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

@receiver(post_save, sender=Contact)
def contact(instance, *args, **kwargs):
    send_contact(f"ФИО: {instance.name}\nНомер: {instance.number}")