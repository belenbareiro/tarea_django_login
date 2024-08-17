from django.urls import path  # type: ignore

from . import views

app_name = "user"

urlpatterns = [
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("userdetail", views.userdetail, name="userdetail"),
    path("edit", views.edit, name="edit"),
    path("change_password", views.change_password, name="change_password"),  # noqa
    path("delete", views.delete, name="delete"),
]
