from django.urls import path
from .views import *

app_name = 'science'

urlpatterns = [
    # Pour les Revue
    path('', list_revue, name='list_revue'),
    path('list_revue_admin/', list_revue_admin, name='list_revue_admin'),
    path('saisir_revue/', saisir_revue, name='saisir_revue'),
    path('detail_revue/<int:revue_id>/', detail_revue, name='detail_revue'),
    path('details_revue_admin/<int:revue_id>/', details_revue_admin, name='details_revue_admin'),
    path('modifie_revue/<int:revue_id>/', modifie_revue, name='modifie_revue'),
    path('supprime_revue/<int:revue_id>/', supprime_revue, name='supprime_revue'),

    # Pour les commentaires
    path('ajouter_commentaire_revue/<int:revue_id>/', ajouter_commentaire_revue, name='ajouter_commentaire_revue'),
    path('liste_commentaire_revue/<int:revue_id>/', liste_commentaire_revue, name='liste_commentaire_revue'),

    # Pour les likes
    path('revue_like/', revue_like, name='revue_like'),

    # Pour telecharger
    path('telecharger_document_revue/<int:revue_id>', telecharger_document_revue, name='telecharger_document_revue'),
]