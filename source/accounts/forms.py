from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=150, required=False, label="Email")
    birth_date = forms.DateField(label='Дата рождения', required=False,)
    avatar = forms.ImageField(label='Аватар', required=False,)
    phone_number = forms.CharField(max_length=150, label="Контактный телефон")
    text = forms.CharField(max_length=3000, label="Text", required=False,)

    class Meta(UserCreationForm.Meta):
        fields = ["username", "avatar", "first_name", "last_name", "phone_number", "email",
                  "birth_date", "password1", "password2", "text"]


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", 'email']
        labels = {'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
