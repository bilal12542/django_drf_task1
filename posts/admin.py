from django.contrib import admin
from .models import Posts


class AdminPosts(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'owner')


# Register your models here.

admin.site.register(Posts, AdminPosts)
