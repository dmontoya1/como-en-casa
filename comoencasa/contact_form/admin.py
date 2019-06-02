from django.contrib import admin

from .models.contact_form import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('full_name', 'email', 'get_contact_type_display')
    search_fields = ('full_name', 'email')