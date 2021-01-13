from django.shortcuts import render
from django.http import HttpResponse

def portfolio_home(request):
    return render(request, 'Portfolio_website/Portfolio_home.html')
