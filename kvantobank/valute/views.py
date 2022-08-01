from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Valute
from .forms import TranzactionForms
from request_card.models import ScanedCard
from party.models import Party

def valute_view(request: HttpRequest):
    valute = Valute.objects.filter()
    return render(request, "valute.html", {
        "valute": valute
    })

def tranzaction_add(request: HttpRequest):
    form = TranzactionForms()
    
    if request.method == "POST":
        valute_name = request.POST.get('valute')
        count = request.POST.get('count')
        count = int(count)
        
        valute_model: Valute = Valute.objects.filter(id=valute_name).first()
        
        plus_money = valute_model.attitude * count
        
        scaned_card: ScanedCard = ScanedCard.objects.order_by('-created_at').first()
        number = scaned_card.number
        party_one: Party = Party.objects.filter(card=number).first()
        party_one.money = party_one.money + plus_money
        party_one.save()

    return render(request, "tranzaction_add.html", {"form": form})


def tranzaction_remove(request: HttpRequest):
    if request.method == "POST":
        count = request.POST.get('count')
        count = int(count)
        
        scaned_card: ScanedCard = ScanedCard.objects.order_by('-created_at').first()
        number = scaned_card.number
        party_one: Party = Party.objects.filter(card=number).first()
        party_one.money = party_one.money - count
        party_one.save()

    return render(request, "tranzaction_remove.html")