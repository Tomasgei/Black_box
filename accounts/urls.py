from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from . forms import SingInForm

urlpatterns = [
    path("signup/", accounts_views.SignUp, name = "signup"),
    path("login/", auth_views.LoginView.as_view(template_name='../templates/accounts/sign-in.html', authentication_form= SingInForm), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(), name = "logout"),
]
