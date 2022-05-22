from django.contrib import admin
from .models import Articles
from .models import Category


# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'full_text')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
