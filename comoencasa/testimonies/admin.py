from django.contrib import admin

from .models.testimonies import Testimonies


@admin.register(Testimonies)
class TestimoniesAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'profesion',)
    search_fields = ('name', 'profesion',)