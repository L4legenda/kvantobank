"""kvantobank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from party.views import *
from request_card.views import *
from valute.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_party),
    path('send_card/', send_card),
    path('link_with_party/', link_card_to_party),
    path('valute/', valute_view),
    path('tranzaction_add/', tranzaction_add),
    path('tranzaction_remove/', tranzaction_remove),
    
]
