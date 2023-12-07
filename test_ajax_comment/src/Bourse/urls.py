
from django.urls import path
from .views import *

app_name = 'bourse'

urlpatterns = [
    # pour les bourse
    path('', liste_bourse, name='liste_bourse'),
    path('liste_bourse_admin/', liste_bourse_admin, name='liste_bourse_admin'),
    path('saisie_bourse/saisie/', saisie_bourse, name='saisie_bourse'),
    path('saisie_bourse/saisie/', saisie_bourse, name='saisie_bourse'),
    path('detail_bourse/<int:bourse_id>/', detail_bourse, name='detail_bourse'),
    path('details_bourse_admin/<int:bourse_id>/', details_bourse_admin, name='details_bourse_admin'),
    path('modifie_bourse/<int:bourse_id>/', modifie_bourse, name='modifie_bourse'),
    path('supprime_bourse/<int:bourse_id>', supprime_bourse, name='supprime_bourse'),

    # pour les postulants
    path('saisir_postulant/<int:bourse_id>/', saisir_postulant, name='saisir_postulant'),
    path('liste_postulant/<int:bourse_id>/', liste_postulant, name='liste_postulant'),

    # pour les commentaires
    path('ajouter_commentaire/<int:bourse_id>/', ajouter_commentaire, name='ajouter_commentaire'),
    path('liste_commentaires/<int:bourse_id>/', liste_commentaires, name='liste_commentaires'),

    # pour les  likes
    path('like/', like, name='like'),
]
