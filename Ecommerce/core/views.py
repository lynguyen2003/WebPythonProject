from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from core.models import Item

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


def checkout(request):
    return render(request, "checkout.html")

class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


# def home(request):
#     return render(request, "home.html")

# def add(request):
    
#     Item.save()
#     return redirect

# def delete(request):

    
#     Item.delete()
#     return redirect

# def detail(request):

    
#     return render(request, 'product.html')
