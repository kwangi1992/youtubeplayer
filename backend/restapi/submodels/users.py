from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User as BaseUser


class User(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


