
from django.shortcuts import render
from django.views.generic import TemplateView

from rooms.models.category import Category


class Home(TemplateView):
    """
    """

    template_name="pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        categories = Category.objects.filter(parent=None)
        context['categories'] = categories
        return context