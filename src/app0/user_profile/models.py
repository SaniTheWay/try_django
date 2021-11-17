from django.contrib.auth import get_user_model
from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.conf import settings

from organizations.models import Organizations
# Create your models here.


User = settings.AUTH_USER_MODEL


class User_profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=CASCADE, default=None, null=True)
    username = models.CharField(max_length=20, default='_')
    first_name = models.CharField(max_length=50, default='_')
    last_name = models.CharField(max_length=50, default='_')
    dob = models.DateField(verbose_name="DoB", default=None)
    org_key = models.ForeignKey(
        Organizations, on_delete=SET_NULL, null=True, blank=False)

    class Meta:
        # otherwise we get "User Profiles in admin"
        verbose_name_plural = "User Profile"
