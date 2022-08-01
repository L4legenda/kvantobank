from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ScanedCard


@csrf_exempt
def send_card(request: HttpRequest):   
    number_card = request.GET.get("number_card")
    
    scaned_card, created = ScanedCard.objects.update_or_create(
        number=number_card, defaults={"number": number_card}
    )
    
    scaned_card.number = number_card
    scaned_card.save()
    
    
    return JsonResponse(data={"message": "success"})
