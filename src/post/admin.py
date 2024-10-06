from django.contrib import admin
from .models import BlogPost
# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'last_updated', 'published')
    list_editable = ('published',)
    list_filter = ('author','published')
    search_fields = ('title','content')
