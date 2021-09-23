from django import forms
from .models import Showcase

class TestForm(forms.Form):
    testname = forms.CharField(label="Your Name", max_length=100)
