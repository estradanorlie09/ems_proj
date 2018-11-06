from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from.models import Event

class HomePageView(TemplateView):
    template_name = "home.html"

class EventListView(ListView):
    model = Event
    template_name = "event_list.html"
    contex_object_name = "event_list"

class EventDetailView(DetailView):
    mode = Event
    template_name = "event_detail.html"
    contex_object_name = "event"
    