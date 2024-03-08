from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, NewsArticle
from .dynamic import news_fetcher
from base.models import NewsArticle
from django.utils import timezone
from .helpers import cleanup_scripts



def Home(request):
    context = {'rooms': Room.objects.all()}
    return render(request, 'index.html', context)

def news(request):
    articles = news_fetcher.get_articles()
    for article in articles:
        try:
            NewsArticle.objects.create(title = article['title'], description=article['description'], created=article['created'], content=article['content'], origin = article['origin'])
        except Exception:
            pass
    
    cleanup_scripts.delete_oldest_items(limit=10, model=NewsArticle)
    articles = NewsArticle.objects.all()
    for article in articles:
        if article.description == "None":
            article.description = "No Available Information"
            article.save()
        elif article.content == "None":
            article.content = "No Available Information"
            article.save()
        else:
            pass
    context = {'news': NewsArticle.objects.exclude(dont_delete=True).all(), 'saved_news': NewsArticle.objects.filter(dont_delete=True)}
    return render(request, 'base/news.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def remove_article(request, id):
    article = NewsArticle.objects.get(id=id)
    article.dont_delete = False
    article.save()
    return redirect("news")

def add_article(request, id):
    article = NewsArticle.objects.get(id=id)
    article.dont_delete = True
    article.save()
    return redirect("news")