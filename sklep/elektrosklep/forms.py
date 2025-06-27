from django import forms
from .models import Produkt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'})
    )

class RejestracjaForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Adres e-mail'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


FORMA_DOSTAWY_CHOICES = [
    ('poczta_polska', 'Kurier Poczta Polska'),
    ('inpost', 'Kurier InPost'),
    ('dhl', 'Kurier DHL'),
]

class ZamowienieForm(forms.Form):
    imie = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    adres = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Adres'})
    )
    kod_pocztowy = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Kod pocztowy'})
    )
    miasto = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Miasto'})
    )
    forma_dostawy = forms.ChoiceField(
        choices=FORMA_DOSTAWY_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Wybierz formę dostawy'})
    )

