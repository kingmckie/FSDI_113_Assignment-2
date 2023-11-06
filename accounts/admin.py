from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (

    ("NONE", {"firls": ("role", "team")}),
    )
fieldsets = UserAdmin.fieldsets = (
    ("NONE", {"fields": ("email", "role", "team")}),
    )
    
list_display = [
        "username", "email", "last_name", "first_name",
        "role", "team", "is_staff"
]

admin.site.register(CustomUser, CustomUserAdmin)