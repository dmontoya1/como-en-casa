
from django.urls import include, path

from . import views

app_name = 'webclient'
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.AboutUs.as_view(), name="about"),
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('services/', views.ServicesListView.as_view(), name='services_list'),
    path('experiences/', views.ExperiencesListView.as_view(), name='experiences_list'),
    path('room/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('experience/<int:pk>/', views.ExperiencesDetailView.as_view(), name='experience_detail'),
    path('contact-form/', views.ContactFormView.as_view(), name='contact_form'),
    path('acommodation-types/', views.AcommodationTypes.as_view(), name='acommodation_types'),
]
