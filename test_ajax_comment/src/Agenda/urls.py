from django.urls import path
from .views import *

app_name = 'agenda'

urlpatterns = [
    path('', index, name='index'),
    path('vue_calendar/', vue_calendar, name='vue_calendar'),
    path('all_events/', all_events, name='all_events'),  
    path('all_events_vue/', all_events_vue, name='all_events_vue'),  
    path('add_event/', add_event, name='add_event'), 
    path('update/', update, name='update'),
    path('remove/', remove, name='remove'),
]
