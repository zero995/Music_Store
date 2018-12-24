from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError

from api import settings
from music import models
from music import serializers


class Command(BaseCommand):
    help = 'Send a email with the information about low stock'

    def handle(self, *args, **kwargs):

        try:
            validate_email(settings.EMAIL_NOFIT_ADMIN)
        except ValidationError:
            return "not valid email"
        try:

            queryset = models.Disc.objects.filter(qty__lte=50)
            data = serializers.DiscsSerializer(queryset, many=True).data
            subject = '[important]These products have a low stock'
            message = 'Hi this is a scheduled message.\n the next products have 50 units or less'
            for item in data:
                message += "\n* Album: " + item["name"] + " by " + item["artist"] + " units in stock: " + str(
                    item["qty"])

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_NOFIT_ADMIN]
            send_mail(subject, message, email_from, recipient_list)
            return "information of low stock was send"
        except Exception as e:
            return e
