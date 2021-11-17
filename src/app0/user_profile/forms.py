from django import forms
from .models import User_profile
from django.contrib.auth import get_user_model

User = get_user_model()
not_allowed_username = ["abc", "ABC", "RED", "red"]


class Userprofile_form(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ['username', 'first_name', 'last_name', 'dob', 'org_key']

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     queryset = User.objects.filter(username__iexact=username)
    #     # in user__iexact -->> thisIsMyUsername == thisismyusername
    #     if queryset.exists():
    #         raise forms.ValidationError(
    #             "This Username is already Exists! Pick another one.")
    #     if username in not_allowed_username:
    #         raise forms.ValidationError("This Username is not Allowed.")
    #     return username
