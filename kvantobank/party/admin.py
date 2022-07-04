from django.contrib import admin
from .models import Party
from django.utils.safestring import mark_safe 

@admin.display(description='QR-CODE')
def generate_qr(obj):
    return mark_safe(f'<img src="http://qrcoder.ru/code/?{obj.token_qr}&4&0">')

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('number_party', 'name', 'money', generate_qr)