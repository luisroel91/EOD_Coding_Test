from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Let's define our custom user admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserModel


class CustomUserAdmin(UserAdmin):

    model = UserModel

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['email', 'username', 'country']


admin.site.register(UserModel, CustomUserAdmin)
