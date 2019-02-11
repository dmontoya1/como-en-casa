from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from . import views

app_name = 'webclient'
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/",TemplateView.as_view(template_name="pages/about.html"),name="about"),
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('services/', views.ServicesListView.as_view(), name='services-list'),
    path('experiences/', views.ExperiencesListView.as_view(), name='experiences-list'),
    path('room/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('experience/<int:pk>/', views.ExperiencesDetailView.as_view(), name='experience-detail'),
    path('contact-form/', views.ContactFormView.as_view(), name='contact_form'),
    
] 


