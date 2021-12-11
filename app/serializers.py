from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token



class Hotel_TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel_Ticket
        fields = '__all__'



class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'subject', 'message')
