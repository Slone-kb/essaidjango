from django import forms
from produits.models import Produits


#class pour formulaire issue du model de produitq
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
    
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Description...'}),
            'prix': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            }
        help_texts={
            'active': 'cocher pour activer et echocher pour deactiver le produit',
            'live': 'cocher pour rendre leproduit visible et dechocher pour le rendre invisible sur site',
        }

#class pour le formolaire issue de django
class PureProduitsForm(forms.Form):
    nom=forms.CharField(max_length=100, widget=forms.TextInput(attrs=
                                                               {'placeholder': 'Nom du produit'}), 
                                                               label='nom du produit')
    description=forms.CharField(widget=forms.Textarea(attrs=
                                                      {'rows':10, 'cols':50, 
                                                       'placeholder':'Description du produit'}), 
                                                       label='description',
                                                        required=False)
    prix = forms.DecimalField(
        max_digits=10,       # Nombre total de chiffres autorisés (partie entière + décimales)
        decimal_places=2,    # Force exactement 2 chiffres après la virgule
        help_text="Il doit avoir deux chiffres après la virgule (ex: 19.99)",
        label="Prix",
        initial= 12.67,
    )
    active=forms.BooleanField(
        required=False,
        label='activer le produit'

    )
    live=forms.BooleanField(
        required=False,
        label='live'
    )


    def clean_nom(self, *args, **kwargs):
        nom=self.cleaned_data.get('nom') 
        if nom !=nom.capitalize():
            raise forms.ValidationError("le nom du produit doit commencer par une lettre majuscule")
        return nom #capitalize la premiere lettre du nom de produit

    def clean_prix(self, *args, **kwargs):
        prix=self.cleaned_data.get('prix')
        if prix <= 0.00:
            raise forms.ValidationError("le prix du produit doit etre superieur a 0")
        return prix