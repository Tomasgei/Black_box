from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SingInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SingInForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={
        "class": "form-control",
        "type" : "text",
        "placeholder": "Enter Username"
    }))

    password = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type" : "password",
        "placeholder": "Enter Password"
    }))


class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={
        "class": "form-control",
        "type" : "text",
        "placeholder": "Type Username"
    }), label="Your Email")

    email = forms.CharField(max_length=200, required=True,widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type" : "email",
        "placeholder": "example@company.com"
    }), label="Your Email")

    password1 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type" : "password",
        "placeholder": "Password"
    }), label="Your Password")

    password2 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type" : "password",
        "placeholder": "Confirm Password"
    }), label="Confirm Password")

    class Meta:
        model = User
        fields = ("username","email","password1","password2")



