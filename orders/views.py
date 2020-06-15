from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {"user": request.user}
    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def register(request):

    form = UserCreationForm()
    if request.method == "POST":
        
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()

            if user is not None:
                return HttpResponseRedirect(reverse("index"))

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "orders/register.html", {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))