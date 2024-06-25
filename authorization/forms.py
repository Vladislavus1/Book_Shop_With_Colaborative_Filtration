from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': "Ім'я користувача",
            'email': "Пошта",
            'password1': "Пароль",
            'password2': "Підтверження паролю"
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password2'})
        }