from django.db import models

# Create your models here.

class Produits(models.Model):
    nom=models.CharField(max_length=1000)
    description=models.TextField(blank=True, null=True)
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    active=models.BooleanField()
    live=models.BooleanField()