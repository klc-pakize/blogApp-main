from django.contrib import admin
from .models import Category, Blog, Comment, Likes
# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)
