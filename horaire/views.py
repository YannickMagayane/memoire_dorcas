from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Horaire, Departement, Salles
from .forms import DepartementForm, SallesForm


class HoraireListView(ListView):
    model = Horaire
    template_name = 'horaire_list.html'
    context_object_name = 'horaires'
    ordering = ['date_creation', 'jour', 'heure_debut']

class HoraireCreateView(CreateView):
    model = Horaire
    template_name = 'horaire_form.html'
    fields = ['jour', 'heure_debut', 'heure_fin', 'cours', 'promotion', 'salles', 'date_creation']
    success_url = reverse_lazy ("horaire-create")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'non_authorized.html')  # Affichez la page de non autorisation
        return super().dispatch(request, *args, **kwargs)


class DepartementCreateView(CreateView):
    model = Departement
    form_class = DepartementForm
    template_name = 'departement_form.html'
    success_url = reverse_lazy("departement-create")  # Personnalisez cette URL de redirection

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'non_authorized.html')  # Affichez la page de non autorisation
        return super().dispatch(request, *args, **kwargs)


class SallesCreateView(CreateView):
    model = Salles
    form_class = SallesForm
    template_name = 'salles_form.html'
    success_url = reverse_lazy("salles-create")  # Personnalisez cette URL de redirection

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'non_authorized.html')  # Affichez la page de non autorisation
        return super().dispatch(request, *args, **kwargs)


class DepartementListView(ListView):
    model = Departement
    template_name = 'departement_list.html'
    context_object_name = 'departements'

class SallesListView(ListView):
    model = Salles
    template_name = 'salles_list.html'
    context_object_name = 'salles'