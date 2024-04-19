from django.shortcuts import render, redirect
from .models import Product, WomenProduct, NewArrivalsProduct
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def products(request):
    return render(request, 'products.html')

def test1(request):
    return render(request, 'test1.html')

def register(request):
    return render(request, 'register.html')

def shoppingbag(request):
    return render(request, 'shoppingbag.html')

def support(request):
    return render(request, 'support.html')

def collections(request):
    return render(request, 'menu/collections.html')

def men(request):
    products = Product.objects.all()
    return render(request, 'menu/men.html', {'products': products})

def women(request):
    women_products = WomenProduct.objects.all()
    return render(request, 'menu/women.html',  {'women_products': women_products})

def newarrivals(request):
    new_arrivals_products = NewArrivalsProduct.objects.all()
    return render(request, 'menu/newarrivals.html',  {'new_arrivals_products': new_arrivals_products})

