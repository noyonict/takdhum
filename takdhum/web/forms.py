from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"User Name", 'value':""}))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"e-mail", 'value':""}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'value':''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password', 'value':''}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserMessageForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.Textarea()


