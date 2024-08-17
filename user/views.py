from django.shortcuts import render  # type: ignore
from django.shortcuts import redirect  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib.auth import login as auth_login  # type: ignore # noqa
from django.contrib import messages  # type: ignore
from .forms import (
    UserCreationForm,
    UserLoginForm,
    UserUpdateForm,
    UserUpdatePasswordForm,
)
from .models import User

# from django.http import HttpResponse


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
            user = User.objects.filter(email=email).first()
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


# @login_required
def userdetail(request):
    # print(request.user)
    try:
        _user = User.objects.get(pk=request.session["_auth_user_id"])
        return render(request, "userdetail.html", {"user": _user})
    except Exception:
        return render(request, "userdetail.html")


# @login_required
def edit(request):
    try:
        _user = User.objects.get(pk=request.session["_auth_user_id"])
    except Exception:
        messages.error(request, "Please login first.")
        return render(request, "userdetail.html")
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=_user)
        if form.is_valid():
            form.save()
            return redirect("user:userdetail")
    else:
        form = UserUpdateForm(instance=_user)

    return render(request, "edit.html", {"form": form})


# @login_required
def delete(request):
    try:
        _user = User.objects.get(pk=request.session["_auth_user_id"])
    except Exception:
        messages.error(request, "Please login first.")
        return render(request, "userdetail.html")
    if request.method == "POST":
        _user.delete()
        return redirect("user:login")
    return render(request, "delete.html")


def change_password(request):
    # print(request.user)
    try:
        _user = User.objects.get(pk=request.session["_auth_user_id"])
    except Exception:
        messages.error(request, "Please login first.")
        return render(request, "userdetail.html")
    if request.method == "POST":
        form = UserUpdatePasswordForm(data=request.POST)
        if form.is_valid():
            _old_password = form.cleaned_data["old_password"]
            if not _user.check_password(_old_password):
                form.add_error("old_password", "Incorrect password")
                return redirect("user:change_password")
            _user.set_password(form.cleaned_data["new_password"])
            _user.save()
            messages.success(request, "Password changed successfully.")
            return redirect("user:login")
    else:
        form = UserUpdatePasswordForm()

    return render(request, "change_password.html", {"form": form})


def logout(request):
    return redirect("user:login")
