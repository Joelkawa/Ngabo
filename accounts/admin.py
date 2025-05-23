from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm


# Register your models here.
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'fathers_name',
            'mothers_name',
            'address',
            'is_superuser',
    ]

admin.site.register(CustomUser,CustomUserAdmin)



