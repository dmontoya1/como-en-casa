from django.contrib import admin

from .models.services import Services
from .models.services_images import ServicesImage
from .models.services_option import ServicesOption


class ServicesOptionInline(admin.StackedInline):
    """
    """

    model = ServicesOption
    extra = 0


class ServicesImageInline(admin.StackedInline):
    """
    """

    model = ServicesImage
    extra = 0


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    inlines = [ServicesOptionInline, ServicesImageInline]
