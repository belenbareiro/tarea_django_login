from django.shortcuts import render  # type: ignore
from django.shortcuts import redirect  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib.auth import authenticate, login as auth_login  # type: ignore # noqa
from django.contrib import messages  # type: ignore
from .forms import (
    UserCreationForm,
    UserLoginForm,
    UserUpdateForm,
    UserUpdatePasswordForm,
)


# Register user
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = UserCreationForm()

    params = {"form": form}
    return render(request, "signup.html", params)


# Login
def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request, username=email, password=password
            )  # Use 'username' to pass email
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome {user.username}!")
                return redirect("tasks:index")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserLoginForm()

    params = {"form": form}
    return render(request, "login.html", params)


@login_required
def userdetail(request):
    return render(request, "userdetail.html")


@login_required
def edit(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user:userdetail")
    return render(request, "edit.html")


@login_required
def delete(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("user:login")
    return render(request, "delete.html")


def change_password(request):
    if request.method == "POST":
        form = UserUpdatePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data["new_password"])
            user.save()
            return redirect("user:login")
    return render(request, "change_password.html")


def logout(request):
    return redirect("user:login")
