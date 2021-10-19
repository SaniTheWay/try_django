from decimal import Decimal
from threading import active_count
from django import forms
from django.db.backends.base import features
from django.db.models import fields
from django.forms.fields import CharField
from .models import Showcase

not_allowed_words = ["bad", "words", "aren't", "allowed"]


class ShowcaseForm(forms.ModelForm):
    class Meta:
        model = Showcase
        fields = [
            'title',
            'description',
            'active',
            'featured',
            'project_img',
            'project_link',
        ]

    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 3:
            raise forms.ValidationError("too short title")
        return data

    def clean_description(self):
        data = self.cleaned_data.get('description')
        if any(not_allowed_words in data for not_allowed_words in data):
            raise forms.ValidationError("bad words are not allowed.")
        return data


# PRE Built Django 'Form' from 'form' Module


# class RawShowcaseForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     active = forms.ChoiceField(required=False)
#     featured = forms.BooleanField()
#     project_img = forms.ImageField()
#     project_link = forms.URLField()
