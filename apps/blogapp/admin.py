from django.contrib import admin
from .models import Article

class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Article, TagAdmin)
