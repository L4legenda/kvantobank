from django.contrib import admin
from .models import ScanedCard


@admin.register(ScanedCard)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('number', 'created_at')
    ordering = ("-created_at",)

