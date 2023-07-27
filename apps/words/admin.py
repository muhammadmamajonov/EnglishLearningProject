from django.contrib import admin
from .models import *


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['id', 'unit']
    list_display_links = ['id', 'unit']