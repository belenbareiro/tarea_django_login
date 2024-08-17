from django.shortcuts import render  # type: ignore
from django.shortcuts import redirect  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib.auth import authenticate, login as auth_login  # type: ignore # noqa
from django.contrib import messages  # type: ignore
from .forms import UserCreationForm, UserLoginForm


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
def showaccountdetails(request):
    return render(request, "showaccountdetails.html")


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


def logout(request):
    return redirect("user:login")
