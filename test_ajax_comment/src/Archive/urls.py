from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'archive'

urlpatterns = [
   # for archive
   path('', liste_archive, name='liste_archive'),
   path('saisie_archive/', saisie_archive, name='saisie_archive'),
   path('liste_archive_admin/', liste_archive_admin, name='liste_archive_admin'),
   path('detail_archive/<int:archive_id>/', detail_archive, name='detail_archive'),
   path('detail_archive_admin/<int:archive_id>/', detail_archive_admin, name='detail_archive_admin'),
   path('modifie_archive/<int:archive_id>/', modifie_archive, name='modifie_archive'),
   path('supprime_archive/<int:archive_id>/', supprime_archive, name='supprime_archive'),

   # pour les commentaires
   path('ajouter_commentaire_archive/<int:archive_id>/', ajouter_commentaire_archive, name='ajouter_commentaire_archive'),
   path('liste_comment_archive/<int:archive_id>/', liste_comment_archive, name='liste_comment_archive'),


   # like for event
   path('archive_like/', archive_like, name='archive_like'),

   # Pour telecharger
   path('telecharger_document_archive/<int:archive_id>', telecharger_document_archive, name='telecharger_document_archive'),
] 