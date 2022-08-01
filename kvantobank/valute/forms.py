from cProfile import label
from django import forms
from .models import Tranzaction

class TranzactionForms(forms.ModelForm):
    class Meta:
        model = Tranzaction
        fields = ('valute', 'count')
        labels = {
            "valute": "Валюта",
            "count": "Количество",
        }