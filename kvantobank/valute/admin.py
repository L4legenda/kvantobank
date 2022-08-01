from django.contrib import admin
from .models import Valute

@admin.register(Valute)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'attitude')
    ordering = ("name",)