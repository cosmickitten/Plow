from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Domain
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
                'time', 
              'title', 
              'intro', 
              'content',
              'summary',
              'is_published',
              'category',
              'url',
              'domain',
              )
    readonly_fields = ('time', 'title', 'intro', 'content','summary','url','domain')
    list_display = ('id', 'title', 'time','url','domain')
    list_display_links = ('title',)
    ordering = ('-time', 'title')
    search_fields = ('title',)
    list_per_page = 50



@admin.register(Domain)
class DomainleAdmin(admin.ModelAdmin):
    fields = (
                'id',
                'name', 
              )
    list_display = ('id','name')