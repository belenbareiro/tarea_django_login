from django.shortcuts import render  # type: ignore
from django.shortcuts import redirect  # type: ignore
from .forms import UserCreationForm, UserLoginForm

# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = UserCreationForm()

    params = {"form": form}

    return render(request, "login.html", params)


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
