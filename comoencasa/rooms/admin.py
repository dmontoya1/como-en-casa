from django.contrib import admin

from .models.rooms import Room
from .models.room_items import RoomItems
from .models.category import Category


class RoomItemsInline(admin.StackedInline):
    """
    """

    model = RoomItems
    extra = 1



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'code', 'category', 'agent',)
    search_fields = ["name", "code"]
    inlines = [RoomItemsInline, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'parent')
    search_fields = ["name", ]
