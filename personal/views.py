from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {}
    return render (request, "personal/home.html", context)

