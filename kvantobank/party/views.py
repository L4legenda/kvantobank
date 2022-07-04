from django.shortcuts import render
from django.http import HttpRequest
from .models import *

# Create your views here.
def list_party(request: HttpRequest):
    party = Party.objects.all().order_by('-money')
    return render(request, "index.html", {
        "party": party
    })