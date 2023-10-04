from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "••••••••"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "••••••••"}))

    class Meta:
        model = User
        fields = ["username"]
        labels = {
            "username": "Username"
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "Enter Your Username"})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "Enter Your Username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder": "••••••••"}))
