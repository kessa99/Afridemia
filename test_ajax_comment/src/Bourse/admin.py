from .models import Bourse, Comment
from django.contrib import admin

admin.site.register(Bourse)


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['auteur', 'date']