from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from core.models import Book, Author, Genre, User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'email': forms.EmailField}


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'
        field_classes = {'email': forms.EmailField}

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error('username', 'Неверный логин или пароль')
        return cleaned_data


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class FilterForm(forms.Form):
    price_min = forms.FloatField(required=False, label='Максимальная цена:')
    price_max = forms.FloatField(required=False, label='Минимальная цена:')
    CHOICES = (
        ("price_desc", "По убыванию цены"),
        ("price_asc", "По возрастанию цены"),
    )
    sorting = forms.ChoiceField(choices=CHOICES, label='Сортировать:')
