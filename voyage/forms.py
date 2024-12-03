from django import forms
from .models import Voyage

class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = ('NomChauffeur', 'plaque', 'NbrPlaceVide', 'VilleDepart', 'VilleArrivee', 'heureDepart',  'Prix')

    def __init__(self, *args, **kwargs):
        super(VoyageForm, self).__init__(*args, **kwargs)
        self.fields['NomChauffeur'].widget.attrs['placeholder'] = 'Nom du chauffeur'
        self.fields['plaque'].widget.attrs['placeholder'] = 'Plaque d\'immatriculation'
        self.fields['NbrPlaceVide'].widget.attrs['placeholder'] = 'Nombre de places vides'
        self.fields['VilleDepart'].widget.attrs['placeholder'] = 'Ville de départ'
        self.fields['VilleArrivee'].widget.attrs['placeholder'] = 'Ville d\'arrivée'
        self.fields['heureDepart'].widget.attrs['placeholder'] = 'Heure de départ'
        self.fields['Prix'].widget.attrs['placeholder'] = 'Prix'