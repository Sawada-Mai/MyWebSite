from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Portfolio, Album, News

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def home(request):
    new_photo = Album.objects.order_by('-add_date').first()
    # news = News.objects.all()
    return render(request, 'polls/home.html', {'new_photo': new_photo})

def photos(request):
    photo = Album.objects.all()
    return render(request, 'polls/photo.html', {'photo': photo})

def portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'polls/portfolio.html', {'portfolio': portfolio})

def portfolio_details(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request,'polls/portfolio_details.html', {'portfolio': portfolio})

