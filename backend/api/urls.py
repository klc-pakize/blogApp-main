from django.urls import path
from .views import BlogView, CategoryView, CommentView, LikesView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', CategoryView)
router.register('blogs', BlogView)
router.register('comments', CommentView)
router.register('likes', LikesView)

urlpatterns = [
    
] + router.urls
