from django.shortcuts import render
from django.http import HttpRequest
from .models import *
from request_card.models import ScanedCard

# Create your views here.
def list_party(request: HttpRequest):
    party = Party.objects.all().order_by('-money')
    return render(request, "index.html", {
        "party": party
    })

def link_card_to_party(request: HttpRequest):
    party = Party.objects.all().order_by('number_party')
    if request.method == "POST":
        scaned_card: ScanedCard = ScanedCard.objects.order_by('-created_at').first()
        number = scaned_card.number
        number_party = request.POST.get("number_party")
        party_one: Party = Party.objects.filter(number_party=number_party).first()
        party_one.card = number
        party_one.save()
    return render(request, "link_with_party.html", {
        "party": party
    })
