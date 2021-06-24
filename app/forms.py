from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class MyUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('username', )


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
