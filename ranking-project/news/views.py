from django.shortcuts import render
from .models import Article

from .models import Reporter

def landing(request):
	articles = (Article.objects.all().order_by('pub_date')[:10])

	context = {'recent_articles': articles}
	return render(request, 'landing.html', context)

def base(request):
	return render(request, 'base.html', context)