# check for unique emails & usernames
# TUTORIAL FROM https://www.youtube.com/watch?v=x8yxM7rCvEc
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *
User = get_user_model()
not_allowed_username = ["abc", "ABC", "RED", "red"]

# ---------------------------------------------------------------------REGISTRATION FORM--------------------------------------------------


class Registermodelform(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",

        ]

    def save(self, commit=True):
        user = super(Registermodelform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=username)
        # in user__iexact -->> thisIsMyUsername == thisismyusername
        if queryset.exists():
            raise forms.ValidationError(
                "This Username is already Exists! Pick another one.")
        if username in not_allowed_username:
            raise forms.ValidationError("This Username is not Allowed.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        queryset = User.objects.filter(username__iexact=email)
        # in user__iexact -->> thisIsMyUsername == thisismyusername
        if queryset.exists():
            raise forms.ValidationError("This Email is already in Use!.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'org_name', 'web_link']


class RegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    organization = forms.CharField(label='Organization Name', max_length=50)

    email = forms.EmailField()

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                # these are HTML attributes

                "class": "form-control",
                "id": "user-password"
            }
        )  # widget = https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                # these are HTML attributes

                "class": "form-control",
                "id": "user-confirm-password"
            }
        )  # widget = https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=username)
        # in user__iexact -->> thisIsMyUsername == thisismyusername
        if queryset.exists():
            raise forms.ValidationError(
                "This Username is already Exists! Pick another one.")
        if username in not_allowed_username:
            raise forms.ValidationError("This Username is not Allowed.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        queryset = User.objects.filter(username__iexact=email)
        # in user__iexact -->> thisIsMyUsername == thisismyusername
        if queryset.exists():
            raise forms.ValidationError("This Email is already in Use!.")
        return email


#  ----------------------------------------------------------LOGIN FORM---------------------------------------------------------------

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                # these are HTML attributes

                "class": "form-control",
                "id": "user-password"
            }
        )  # widget = https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=username)
        # in user__iexact -->> thisIsMyUsername == thisismyusername
        if not queryset.exists():
            raise forms.ValidationError("This is Invalid user.")
        return username
