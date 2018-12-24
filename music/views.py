# Create your views here.
import secrets

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db import IntegrityError
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView

from api import settings
from . import models
from . import serializers


class ListDiscsView(APIView):
    def get(self, request):
        genere = request.GET.get("genere")

        if genere is None:
            queryset = models.Disc.objects.all()

        else:
            queryset = models.Disc.objects.filter(Q(genere__name=genere) | Q(subgeneres__name=genere))
        data = serializers.DiscsSerializer(queryset, many=True).data
        return JsonResponse(data, safe=False)


def email(request):
    email_to = request.POST.get('email')
    name = request.POST.get('name')
    status = "ok"
    if email_to is None or name is None:
        return Response({'error': 'Please provide both name and email'},
                        status=HTTP_400_BAD_REQUEST)

    try:
        validate_email(email_to)
    except ValidationError:
        status = "not valid email"

    if status == "ok":
        try:
            key = secrets.token_urlsafe(64)
            models.User.objects.create(name=name, email=email_to, apikey=key)

        except IntegrityError as e:
            status = "already registered"
            pass

    if status == "ok":

        try:
            subject = 'Thank you for registering to our site'
            message = 'this is your api key\n' + str(key)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_to]
            send_mail(subject, message, email_from, recipient_list)
            status = "your api key are in your inbox."
        except Exception as e:
            status = "fail"
        pass

    return JsonResponse({'status': status})


class register(APIView):
    """this endpoint return the status of self register form"""

    def post(self, request):
        return email(request)
