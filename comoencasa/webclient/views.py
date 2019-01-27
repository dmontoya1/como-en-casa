
from django.shortcuts import render
from django.views.generic import TemplateView

from rooms.models.category import Category
from testimonies.models.testimonies import Testimonies


class Home(TemplateView):
    """
    """

    template_name="pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        categories = Category.objects.filter(parent=None)
        testimonies = Testimonies.objects.all()
        context['categories'] = categories
        context['testimonies'] = testimonies
        return context
