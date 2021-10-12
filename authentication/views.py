from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignupForm
from django.shortcuts import redirect, render, reverse
from users.models import MyUser


# Create your views here.
def signup_view(request):
    template_name = "signup.html"
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            login(request, user)
            return redirect(reverse("home"))
    return render(request, template_name, {"form": form, "header": "Signup"})


def login_view(request):
    template_name = "login.html"
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
    return render(request, template_name, {"form": form, "header": "Login"})


def logout_view(request):
    logout(request)
    return redirect(reverse("home"))