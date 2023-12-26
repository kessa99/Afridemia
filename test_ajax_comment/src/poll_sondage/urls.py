from django.urls import path
from .views import *

app_name = 'my_question'

urlpatterns = [
    path('', liste_sondage_admin_index, name='liste_sondage_admin_index'),
    path('<str:pk>/', details_poll, name='details_poll'),
    path('create_poll_index/', create_poll_index, name="create_poll_index"),
    path('add_vote/<str:id>/', add_vote, name='add_vote'),
]
