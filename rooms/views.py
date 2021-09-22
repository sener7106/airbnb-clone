from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """Home View Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ Room Detail Definition"""
    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    country = request.GET.get("country", "KR")
    room_type = request.GET.get("country", 0)
    
    form = {"city": city, "s_country": country, "s_room_type": room_type}
    
    choices = {"countries": countries, "room_types": room_types}
    
    return render(request,
                  "rooms/search.html",
                  {**form, **choices})
    