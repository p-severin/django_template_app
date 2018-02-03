from django import forms
from django.forms import ModelForm
from .models import MenuOption

class MenuForm(forms.Form):

    title = forms.CharField(max_length=200)
