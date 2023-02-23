from django.shortcuts import render
from .models import Category, Blog, Comment, Likes
from .serializers import CategorySerializer, BlogSerializer, CommentSerializer, LikesSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly, IsOwnerOrReadOnlyComment
from rest_framework.response import Response



# Create your views here.

class CategoryView(ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]  # category işlemleriniden sadece get işlemini her login olan kullanıcı görebilir ama put post delete işlemlerini sadece staff user yapabilir.
     

class BlogView(ModelViewSet):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Bloglarda get işlemini login olan her kullanıcı yapabilecek update ve delete işlemlerini yalnızca blog sahibi yapabilecek

    def get_queryset(self):
        return super().get_queryset().filter(status='p')  # sadece yayın statusu public olan blogları yayınla
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.post_views+=1
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
class CommentView(ModelViewSet):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnlyComment]  # her kullanıcı kendi yorumunu düzenleyebilecek herkesin yorumunu görüntüleyebilecek

class LikesView(ModelViewSet):

    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    