from decimal import Decimal
from threading import active_count
from django import forms
from django.db.backends.base import features
from django.db.models import fields
from django.forms.fields import CharField
from .models import Showcase

class ShowcaseForm(forms.ModelForm):
    class Meta:
        model = Showcase
        fields = [
            'title',
            'description',
            # 'summary',
            'active',
            'featured',
            'project_img',
            'project_link'
        ]

# PRE Built Django 'Form' from 'form' Module
class RawShowcaseForm(forms.Form):
    title       =forms.CharField()
    description =forms.CharField()
    active      =forms.ChoiceField(required=False)
    featured    =forms.BooleanField()
    project_img =forms.ImageField()
    project_link=forms.URLField()