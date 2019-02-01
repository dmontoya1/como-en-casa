
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rooms.models.category import Category
from rooms.models.rooms import Room
from testimonies.models.testimonies import Testimonies


class Home(TemplateView):
    """
    """

    template_name="pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        categories = Category.objects.filter(parent=None)
        rooms = Room.objects.all()
        testimonies = Testimonies.objects.all()
        context['categories'] = categories
        context['rooms'] = rooms
        context['testimonies'] = testimonies
        return context


class RoomListView(ListView):
    """
    """

    model = Room
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(~Q(parent=None))
        context['categories'] = categories
        return context


class RoomDetailView(DetailView):
    """
    """

    model = Room
