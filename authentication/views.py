from django.shortcuts import render
from django.views.generic import View
from authentication.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        form = SignUpForm(label_suffix="")
        return render(request, "authentication/sign-up.html", {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))

        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return render(request, "authentication/sign-up.html", {'form': form})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        form = LoginForm(label_suffix="")
        return render(request, "authentication/login.html", {'form': form})

    def post(self, request, *args, **kawrgs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))

        form = LoginForm(label_suffix="", request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("home"))

        return render(request, "authentication/login.html", {'form': form})


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        logout(request)
        return HttpResponseRedirect(reverse("login"))
