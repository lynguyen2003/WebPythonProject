from django.shortcuts import render

def products(request):
    return render(request, "product.html")


def checkout(request):
    return render(request, "checkout.html")


def home(request):
    return render(request, "home.html")
