from django.contrib import admin

from .models.services import Services
from .models.option_service import OptionServices


class OptionServicesInline(admin.StackedInline):
    """
    """

    model = OptionServices
    extra = 0


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    inlines = [OptionServicesInline, ]
