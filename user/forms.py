from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'age', 'country')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = ('username', 'password', 'email', 'country')