from django.urls import path
from . import views



urlpatterns = [
    path('', views.HoraireListView.as_view(), name='horaire-list'),
    path('creer/horaire/', views.HoraireCreateView.as_view(), name='horaire-create'),
    path('creer/salle/', views.SallesCreateView.as_view(), name='salles-create'),
    path('creer/departement/', views.DepartementCreateView.as_view(), name='departement-create'),
    path('liste/departement/', views.DepartementListView.as_view(), name='departement-list'),
    path('liste/salles', views.SallesListView.as_view(), name='salles-list'),
    path('horaire/<int:pk>/',views.HoraireUpdate.as_view(),name='modifier'),
]
