from django.contrib import admin

from .models import Article
from .models import Reporter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	pass


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
	pass
