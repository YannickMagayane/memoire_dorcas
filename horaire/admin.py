from django.contrib import admin
from .models import Departement, Salles, Horaire

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ['departement', 'filiere', 'promotion']

@admin.register(Salles)
class SallesAdmin(admin.ModelAdmin):
    list_display = ['numero_salle', 'nom_salle', 'promotion']

@admin.register(Horaire)
class HoraireAdmin(admin.ModelAdmin):
    list_display = ['jour', 'heure_debut', 'heure_fin', 'cours', 'promotion', 'salles', 'date_creation']
