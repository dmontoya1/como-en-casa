
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from contact_form.models.contact_form import ContactForm
from experiences.models.experiences import Experiences
from general_config.models import CompanyInfo
from rooms.models.category import Category
from rooms.models.rooms import Room
from services.models.services import Services
from testimonies.models.testimonies import Testimonies


class Home(TemplateView):
    """
    """

    template_name = "webclient/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        categories = Category.objects.filter(parent=None)
        rooms = Room.objects.all()
        testimonies = Testimonies.objects.all()
        services = Services.objects.all()
        experiences = Experiences.objects.all()
        context['categories'] = categories
        context['rooms'] = rooms
        context['testimonies'] = testimonies
        context['services'] = services
        context['experiences'] = experiences
        return context


class AboutUs(TemplateView):
    """
    """

    template_name = "webclient/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['contact'] = CompanyInfo.objects.first()
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


class ServicesListView(ListView):
    """
    """

    model = Services
    paginate_by = 20


class ServiceDetailView(DetailView):
    """
    """

    model = Services


class ExperiencesListView(ListView):
    """
    """

    model = Experiences
    paginate_by = 20


class ExperiencesDetailView(DetailView):
    """
    """

    model = Experiences


class ContactFormView(TemplateView):
    """
    """

    template_name = 'webclient/contact_form.html'

    def post(self, request):
        c_form = ContactForm(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            contact_type=request.POST['contact_type'],
            message=request.POST['message']
        )
        print (c_form)
        c_form.save()
        messages.add_message(request, messages.INFO, 'Formulario creado exitosamente. Pronto nos pondremos en contacto contigo')
        return HttpResponseRedirect(reverse('webclient:contact_form'))

