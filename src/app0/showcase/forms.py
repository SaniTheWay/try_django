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
            'price',
            'summary',
            'active',
            'featured'
        ]

# PRE Built Django 'Form' from 'form' Module
class RawShowcaseForm(forms.Form):
    title       =forms.CharField()
    description =forms.CharField()
    # prices      =forms.DecimalField()    
    summary     =forms.CharField()
    # active      =forms.ChoiceField()
    featured    =forms.BooleanField()

# # PRACTICE FORM
# class TestForm(forms.Form):
#     testname = forms.CharField(label="Your Name", max_length=100)
