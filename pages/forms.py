from django import forms
from produits.models import Produits

class ProduitsForms(forms.ModelForm):
    class Meta:
        model=Produits
        fields=[
            'nom',
            'prix',
            'description',
            'active',
            'live'

        ]

