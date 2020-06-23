from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flavor, Crust, Size, Extra, Pizza
from django.db.models import Sum

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})

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
    username = request.user
    context = {
        "user": request.user,
        "flavors": Flavor.objects.all(),
        "crusts": Crust.objects.all(),
        "sizes": Size.objects.all(),
        "extras": Extra.objects.all(),
        "pizzas": Pizza.objects.all().filter(username=username),
        "orders": Pizza.objects.all().filter(username=username).count(),
        "total_order": Pizza.objects.all().filter(username=username).aggregate(Sum('price'))
        }

    if request.method == 'POST':
        pizza = Pizza.objects.all()
        username = request.user
        extras = request.POST.getlist('extra')
        
        pizza.create(
            id=None,
            pizza_flavor_id = Flavor.objects.get(typeof_flavor=request.POST["flavor"]).id,
            pizza_size_id = Size.objects.get(typeof_size=request.POST["size"]).id,
            pizza_crust_id = Crust.objects.get(typeof_crust=request.POST["crust"]).id,
            username = username,
        )

        current_pizza = Pizza.objects.filter(username=username).last()
        
        if str(current_pizza.pizza_size) == "Small (6.95 €)":
            current_pizza.price = 6.95
        elif str(current_pizza.pizza_size) == "Medium (9.95 €)":
            current_pizza.price = 9.95
        elif str(current_pizza.pizza_size) == "Large (12.95 €)":
            current_pizza.price = 12.95
        current_pizza.price = current_pizza.price + 0.5*len(extras)
        current_pizza.save()
        
        for i in range(len(extras)):
            current_pizza.pizza_extra.add(Extra.objects.get(typeof_extra=extras[i]))

        context = {
            "user": request.user,
            "flavors": Flavor.objects.all(),
            "crusts": Crust.objects.all(),
            "sizes": Size.objects.all(),
            "extras": Extra.objects.all(),
            "pizzas": Pizza.objects.all().filter(username=username),
            "orders": Pizza.objects.all().filter(username=username).count(),
            "total_order": Pizza.objects.all().filter(username=username).aggregate(Sum('price'))
        }

        return render(request, "orders/index.html", context)

    return render(request, "orders/index.html", context)

def cart(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    username = request.user

    if request.method == 'POST':
        if 'delete' in request.POST:
            Pizza.objects.filter(pk=request.POST["delete"]).delete()

        if 'street' in request.POST:
            if request.POST["street"] is "" or request.POST["number_floor"] is "" or request.POST["city_zip"] is "" or request.POST["province"] is "":
                return render(request, "orders/error.html", {"message": "You must provide a valid address for the delivery"})
            else:
                print(request.POST["payment"])
                current_pizza = Pizza.objects.filter(username=username).last()
                current_pizza.street = request.POST["street"]
                current_pizza.number_floor = request.POST["number_floor"]
                current_pizza.city_zip = request.POST["city_zip"]
                current_pizza.province = request.POST["province"]
                current_pizza.payment = request.POST["payment"]
                current_pizza.comments = request.POST["comments"]
                current_pizza.progress = "We have received your order"
                current_pizza.save()

    context = { 
        "user": request.user,
        "flavors": Flavor.objects.all(),
        "crusts": Crust.objects.all(),
        "sizes": Size.objects.all(),
        "extras": Extra.objects.all(),
        "pizzas": Pizza.objects.all().filter(username=username),
        "orders": Pizza.objects.all().filter(username=username).count(),
        "total_order": Pizza.objects.all().filter(username=username).aggregate(Sum('price')),
        "progress": Pizza.objects.all().filter(username=username).last(),
        }
    return render(request, "orders/cart.html", context)
