from django.shortcuts import render
from .models import Category, Blog, Comment, Likes
from .serializers import CategorySerializer, BlogSerializer, CommentSerializer, LikesSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly


# Create your views here.

class CategoryView(ModelViewSet):
    # category işlemleriniden sadece get işlemini her login olan kullanıcı görebilir ama put post delete işlemlerini sadece staff user yapabilir.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    

class BlogView(ModelViewSet):
    # Bloglarda get işlemini login olan her kullanıcı yapabilecek update ve delete işlemlerini yalnızca blog sahibi yapabilecek
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CommentView(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikesView(ModelViewSet):

    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
