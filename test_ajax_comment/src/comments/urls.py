
from django.urls import path
from .views import ajouter_commentaire, liste_commentaires

urlpatterns = [
    # ... autres URLs
    path('liste_commentaires/', liste_commentaires, name='liste_commentaires'),
    path('ajouter_commentaire/', ajouter_commentaire, name='ajouter_commentaire'),
]
