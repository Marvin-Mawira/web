from django.shortcuts import render, HttpResponse
from django.contrib import admin

from django.shortcuts import render, redirect
from .forms import ContactForm

from .models import ContactMessage
# from django.http import HttpResponse, HttpResponseRedirect, HttpRequest


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import BuyNowForm


from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductPurchaseForm

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

def index(request):
    return render(request, 'index.html') #returns the index.html

def fruit(request):
    return render(request, 'fruit.html')

def login(request):
    return render(request, 'login.html')

def service(request):
    return render(request, 'service.html') 



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # Save the form data to the database
            k = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            print(k)
            # Redirect or do something else after successful submission
            return HttpResponse("<h1> Thank you for contacting us</h1>")
        else:
            return HttpResponse("Invalid form submitted")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
 

def product_detail(request):
    return render(request, 'product_detail.html') 


def success(request):
    return render(request, 'success.html') 


# views.py

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = BuyNowForm()

    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        if form.is_valid():
            # Process the purchase (you may want to save the order to a database, etc.)
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            # In a real-world scenario, you would likely integrate with a payment gateway here.
            # For simplicity, we'll just display a success message.
            return render(request, 'success.html', {'total_price': total_price})

    return render(request, 'product_detail.html', {'product': product, 'form': form})


def buy_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductPurchaseForm(request.POST)
        if form.is_valid():
            # Get the data from the form
            product_name = form.cleaned_data['product_name']
            product_price = form.cleaned_data['product_price']
            customer_fname = form.cleaned_data['customer_fname']
            phone_number = form.cleaned_data['phone_number']

            # Create a new product instance with the purchased product details
            purchased_product = Product(name=product_name, price=product_price, fname=customer_fname, number=phone_number)
            purchased_product.save()

            # Redirect or render success page
            return redirect('success')  # Change 'success' to the actual URL name or path

    else:
        form = ProductPurchaseForm()

    return render(request, 'product_detail.html', {'product': product, 'form': form})
