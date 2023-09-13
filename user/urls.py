from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('connexion/', LoginView.as_view(template_name='login.html',next_page='horaire-list'), name='connexion'),
    path('deconnexion/', LogoutView.as_view(next_page='horaire-list'), name='deconnexion'),

]
