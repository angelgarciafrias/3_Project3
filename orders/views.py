from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flavor, Crust, Size, Extra, Pizza

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

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = {
        "user": request.user,
        "flavors": Flavor.objects.all(),
        "crusts": Crust.objects.all(),
        "sizes": Size.objects.all(),
        "extras": Extra.objects.all(),
        }

    if request.method == 'POST':
        pizza = Pizza.objects.all()
        pizza.create(
            id=None,
            pizza_flavor_id = Flavor.objects.get(typeof_flavor=request.POST["flavor"]).id,
            pizza_size_id = Size.objects.get(typeof_size=request.POST["size"]).id,
            pizza_crust_id = Crust.objects.get(typeof_crust=request.POST["crust"]).id,
            quantity = 1,
        )

        Pizza.objects.last().pizzas_extra.add(Extra.objects.get(typeof_extra=request.POST["extra"]))
        return render(request, "orders/index.html", context)

    return render(request, "orders/index.html", context)

def cart(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = {
        "user": request.user,
        "flavors": Flavor.objects.all(),
        "crusts": Crust.objects.all(),
        "sizes": Size.objects.all(),
        "extras": Extra.objects.all(),
        }
    return render(request, "orders/cart.html", context)
