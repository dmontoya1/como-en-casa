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
    path("about/",TemplateView.as_view(template_name="pages/about.html"),name="about",
    ),
    
] 


