from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Category, RegularPizza, SicilianPizza, Toppings, Sub, Pasta, Salad, Rice, UserOrder, SavedCarts
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        
        return render(request, "meals/home.html", {"categories":Category.objects.all})
    else:
        return redirect("meals:login")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "meals/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    return redirect("meals:login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("meals:index")

        return render(request = request,
                          template_name = "meals/register.html",
                          context={"form":form})

    return render(request = request,
                  template_name = "meals/register.html",
                  context={"form":UserCreationForm})

def pizza(request):
    if request.user.is_authenticated:
        return render(request, "meals/pizza.html", context = {"regular_pizza":RegularPizza.objects.all, "sicillian_pizza":SicilianPizza.objects.all , "toppings":Toppings.objects.all, "number_of_toppings":[1,2,3]})
    else:
        return redirect("meals:login")

def pasta(request):
    if request.user.is_authenticated:
        return render(request, "meals/pasta.html", context = {"dishes":Pasta.objects.all})
    else:
        return redirect("meals:login")


def salad(request):
    if request.user.is_authenticated:
        return render(request, "meals/salad.html", context = {"dishes":Salad.objects.all})
    else:
        return redirect("meals:login")


def subs(request):
    if request.user.is_authenticated:
        return render(request, "meals/sub.html", context = {"dishes":Sub.objects.all})
    else:
        return redirect("meals:login")


def rice(request):
    if request.user.is_authenticated:
        return render(request, "meals/rice.html", context = {"dishes":Rice.objects.all})
    else:
        return redirect("meals:login")

def directions(request):
    if request.user.is_authenticated:
        return render(request, "meals/directions.html")
    else:
        return redirect("meals:login")

def hours(request):
    if request.user.is_authenticated:
        return render(request, "meals/hours.html")
    else:
        return redirect("meals:login")

def contact(request):
    if request.user.is_authenticated:
        return render(request, "meals/contact.html")
    else:
        return redirect("meals:login")

def cart(request):
    if request.user.is_authenticated:
        return render(request, "meals/cart.html")
    else:
        return redirect("meals:login")

def checkout(request):
    if request.method == 'POST':
        cart = json.loads(request.POST.get('cart'))
        price = request.POST.get('price_of_cart')
        username = request.user.username
        response_data = {}
        list_of_items = [item["item_description"] for item in cart]

        order = UserOrder(username=username, order=list_of_items, price=float(price), delivered=False) #create the row entry
        order.save() #save row entry in database

        response_data['result'] = 'Order Recieved!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def view_orders(request):
    if request.user.is_superuser:
        #make a request for all the orders in the database
        rows = UserOrder.objects.all().order_by('-time_of_order')
        #orders.append(row.order[1:-1].split(","))

        return render(request, "meals/orders.html", context = {"rows":rows})
    else:
        rows = UserOrder.objects.all().filter(username = request.user.username).order_by('-time_of_order')
        return render(request, "meals/orders.html", context = {"rows":rows})

def mark_order_as_delivered(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        UserOrder.objects.filter(pk=id).update(delivered=True)
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def save_cart(request):
    if request.method == 'POST':
        cart = request.POST.get('cart')
        saved_cart = SavedCarts(username=request.user.username, cart=cart) #create the row entry
        saved_cart.save() #save row entry in database
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def retrieve_saved_cart(request):
    saved_cart = SavedCarts.objects.get(username = request.user.username)
    return HttpResponse(saved_cart.cart)

def check_superuser(request):
    print(f"User super??? {request.user.is_superuser}")
    return HttpResponse(request.user.is_superuser)
