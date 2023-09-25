from django import forms
from .models import Departement, Salles


class SallesForm(forms.ModelForm):
    class Meta:
        model = Salles
        fields = ['numero_salle', 'nom_salle', 'promotion']

    def __init__(self, *args, **kwargs):
        super(SallesForm, self).__init__(*args, **kwargs)

        # Appliquez des classes CSS personnalisées à chaque champ
        self.fields['numero_salle'].widget.attrs.update({'class': 'w-full p-2 border rounded'})
        self.fields['nom_salle'].widget.attrs.update({'class': 'w-full p-2 border rounded'})
        self.fields['promotion'].widget.attrs.update({'class': 'w-full p-2 border rounded'})

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['departement', 'filiere','promotion']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DepartementForm, self).__init__(*args, **kwargs)

        # Appliquez des classes CSS personnalisées à chaque champ
        self.fields['departement'].widget.attrs.update({'class': 'w-full p-2 border rounded'})
        self.fields['filiere'].widget.attrs.update({'class': 'w-full p-2 border rounded'})

        # Cachez le champ 'promotion' s'il n'est pas superutilisateur
        if user and not user.is_superuser:
            self.fields['promotion'].widget = forms.HiddenInput()