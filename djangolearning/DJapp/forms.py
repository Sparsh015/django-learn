from django import forms
from .models import Varity

class VarityForm(forms.Form):
    anime_varity = forms.ModelChoiceField(queryset=Varity.objects.all(), label = "select anime varity")
    