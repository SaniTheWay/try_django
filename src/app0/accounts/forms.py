# check for unique emails & usernames
# TUTORIAL FROM https://www.youtube.com/watch?v=x8yxM7rCvEc
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
not_allowed_username = ["abc", "ABC", "RED", "red"]

# ---------------------------------------------------------------------REGISTRATION FORM--------------------------------------------------


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
