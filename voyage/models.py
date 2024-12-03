from django.db import models
from django.contrib.auth.models import User

class Voyage(models.Model):
    id = models.AutoField(primary_key=True)
    NomChauffeur = models.CharField(max_length=100)
    plaque = models.CharField(max_length=100)
    NbrPlaceVide = models.IntegerField()
    VilleDepart = models.CharField(max_length=100)
    VilleArrivee = models.CharField(max_length=100)
    heureDepart = models.TimeField()
    Prix = models.IntegerField()
    date = models.DateField(auto_now_add=True,blank=True ,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voyages",default=1)
    def __str__(self):
        return self.plaque

class Escale(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name="escales")
    VilleEscale = models.CharField(max_length=100)
    NbrPlaceAjouter = models.IntegerField(null=True)

    def __str__(self):
        return self.voyage.plaque
