from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'index.html', {})


def static_handler(request):
    
    return render(request, 'static_handler.html', {})

