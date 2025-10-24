from django.shortcuts import render, redirect
from .models import MenuCategory, News, Location, Review

def home(request):
    latest_news = News.objects.all().order_by('-created_at')[:3]
    return render(request, 'card/home.html', {'latest_news': latest_news})

def menu(request):
    categories = MenuCategory.objects.prefetch_related('menuitem_set').all()
    return render(request, 'card/menu.html', {'categories': categories})

def news(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'card/news.html', {'news_list': news_list})

def locations(request):
    locations = Location.objects.all()
    return render(request, 'card/locations.html', {'locations': locations})

def reviews(request):
    if request.method == 'POST':
        Review.objects.create(
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            rating=request.POST.get('rating')
        )
        return redirect('reviews')
    
    reviews_list = Review.objects.all().order_by('-created_at')
    return render(request, 'card/reviews.html', {'reviews': reviews_list})