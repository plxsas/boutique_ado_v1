from django.shortcuts import render
<<<<<<< HEAD
from .models import Product, Category


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
=======
from .models import Product
# Create your views here.

def all_products(request):
    """ A view to show all products including  sorting and search queries"""

    products = Products.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
>>>>>>> 88f9860d886e8b8d3dfd9fcd47d21165ff1acbad
