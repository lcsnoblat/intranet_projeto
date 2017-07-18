from django.db import models

# Create your models here.
import pickle
import base64

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField


# class Usuario(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	presidente = models.BooleanField()


# class CredentialsModel(models.Model):
#   id = models.ForeignKey(Usuario, primary_key=True)
#   credential = CredentialsField()


# class CredentialsAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(CredentialsModel, CredentialsAdmin)

