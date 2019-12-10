from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def history(request):
    return render(request, "history.html")

def foods(request):
    return render(request, "foods.html")

def places(request):
    print(request.POST)
    return render(request, "places.html")