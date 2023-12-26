"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', include('myauth.urls')),
    path('bourse/', include('Bourse.urls')),
    path('archive/', include('Archive.urls')),
    path('event/', include('Event.urls')),
    path('sondage/', include('Sondage.urls')),
    path('question/', include('question.urls')),
    path('poll_sondages/', include('poll_sondage.urls')),
    path('science/', include('science.urls')),
]


if settings.DEBUG:
    #a ne pas lancer quand on est en production
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)