from django import forms
from django.db.models import fields
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