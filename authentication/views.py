from django.shortcuts import render, redirect
from django.views.generic import View
from authentication.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from authentication.decorators import if_not_logged_in


@method_decorator(if_not_logged_in(redirect_to="home"), name="dispatch")
class SignUpView(View):
    """
        user creation view
    """
    template_name = "authentication/sign-up.html"

    def get(self, request):
        form = SignUpForm(label_suffix="")
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("home")
        return render(request, self.template_name, {'form': form})


@method_decorator(if_not_logged_in(redirect_to="home"), name="dispatch")
class LoginView(View):
    """
        user login view
    """
    template_name = "authentication/login.html"

    def get(self, request):
        form = LoginForm(label_suffix="")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kawrgs):
        form = LoginForm(label_suffix="", request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")

        return render(request, self.template_name, {'form': form})


@method_decorator(if_not_logged_in(redirect_to="home"), name="dispatch")
class LogoutView(View):
    """
        user logout view
    """
    def get(self, request):
        logout(request)
        return redirect("login")
