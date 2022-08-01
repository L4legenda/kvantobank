from django.contrib import admin
from .models import Party


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_party', 'money', 'card')
    fields = ('number_party', 'name', 'money')