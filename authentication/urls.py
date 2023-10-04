from django.urls import path
from authentication.views import SignUpView, LoginView, LogoutView

urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
