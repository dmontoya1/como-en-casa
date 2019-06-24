from django.contrib import admin

from .models.rooms import Room
from .models.room_images import RoomImages
from .models.room_items import RoomItems
from .models.category import Category
from .models.category_benefits import CategoryBenefits
from .models.category_services import CategoryServices
from .models.sectors import Sector


class RoomItemsInline(admin.StackedInline):
    """
    """

    model = RoomItems
    extra = 1


class RoomImagesInline(admin.StackedInline):
    """
    """

    model = RoomImages
    extra = 1


class CategoryBenefitsInline(admin.StackedInline):
    """
    """

    model = CategoryBenefits
    extra = 0


class CategoryServicesInline(admin.StackedInline):
    """
    """

    model = CategoryServices
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'code', 'category', 'agent', 'available')
    search_fields = ["name", "code"]
    inlines = [RoomItemsInline, RoomImagesInline ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'parent')
    search_fields = ["name", ]
    readonly_fields = ('slug', )
    inlines = [CategoryBenefitsInline, CategoryServicesInline]


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):

    list_display = ('name',)
