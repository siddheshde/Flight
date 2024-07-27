from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Record

# Register/Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

# Add a Record
class CreateRecordForm(forms.ModelForm):
    departure_time = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now
    )

    class Meta:
        model = Record
        fields = ['flight_number', 'airways_name', 'departure_time', 'price', 'email', 'city', 'province', 'country']

# Update a Record
class UpdateRecordForm(forms.ModelForm):
    departure_time = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now
    )

    class Meta:
        model = Record
        fields = ['flight_number', 'airways_name', 'departure_time', 'price', 'email', 'city', 'province', 'country']
