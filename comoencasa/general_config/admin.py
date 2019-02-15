from django.contrib import admin

from .models import Police, CompanyInfo


@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('police_type', )


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    """
    """
