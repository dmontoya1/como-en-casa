from django.contrib import admin

from .models.experiences import Experiences
from .models.experiences_image import ExperiencesImage
from .models.experieces_items import ExperiencesItems


class ExperiencesImageInline(admin.StackedInline):
    """
    """

    model = ExperiencesImage
    extra = 0


class ExperiencesItemsInline(admin.StackedInline):
    """
    """

    model = ExperiencesItems
    extra = 0


@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    inlines = [ExperiencesImageInline, ExperiencesItemsInline]
