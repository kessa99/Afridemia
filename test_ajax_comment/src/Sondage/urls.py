from django.urls import path
from . import views

app_name = 'sondages'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('vote/<int:poll_id>/', views.vote, name='vote'),
    path('results/<int:poll_id>/', views.results, name='results'),
    path('delete/<int:poll_id>/', views.delete_poll, name='delete_poll'),
    path('update/<int:poll_id>/', views.update_poll, name='update_poll'),

]
