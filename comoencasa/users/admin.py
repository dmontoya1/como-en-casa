from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from comoencasa.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = auth_admin.UserAdmin.fieldsets + (("Datos usuario", {"fields": ("document_type", "document_id", "birth_date")}),) 
    list_display = ["email", "first_name", "last_name", "birth_date"]
    search_fields = ["first_name", "last_name"]
