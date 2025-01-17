from django.shortcuts import render

# Create your views here.

# index page
def index(request):
    return render(request, "users/index.html")

# index page
def signin(request):
    return render(request, "users/signin.html")
    

