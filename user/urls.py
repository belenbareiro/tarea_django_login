from django.urls import path  # type: ignore

from . import views

app_name = "user"

urlpatterns = [
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("userdetails", views.showaccountdetails, name="userdetails"),
]
