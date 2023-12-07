from django.urls import path
from .views import *

app_name = 'event'

urlpatterns = [
    # Pour les Event
    path('list_event/', list_event, name='list_event'),
    path('list_event_admin/', list_event_admin, name='list_event_admin'),
    path('saisir_event/', saisir_event, name='saisir_event'),
    path('detail_Event/<int:event_id>/', detail_Event, name='detail_Event'),
    path('details_event_admin/<int:event_id>/', details_event_admin, name='details_event_admin'),
    path('modifie_event/<int:event_id>/', modifie_event, name='modifie_event'),
    path('supprime_event/<int:event_id>/', supprime_event, name='supprime_event'),


    # Pour les Participants
    path('saisir_participant/<int:event_id>/', saisir_participant, name='saisir_participant'),
    path('list_participant/<int:event_id>/', list_participant, name='list_participant'),


    # Pour les commentaires
    path('ajouter_commentaire_event/<int:event_id>/', ajouter_commentaire_event, name='ajouter_commentaire_event'),
    path('liste_commentaires/<int:event_id>/', liste_commentaires, name='liste_commentaires'),

    # Pour les likes
    path('event_like/', event_like, name='event_like'),
]