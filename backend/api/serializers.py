from rest_framework import serializers
from .models import Category, Blog, Comment, Likes

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'time_stamp',
            'content',
            'post',
        )

class LikesSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    class Meta:
        model = Likes
        fields = (
            'id',
            'user_id',
            'post_id',
        )

class BlogSerializer(serializers.ModelSerializer):

    comment_count = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many = True, read_only = True)
    category_name = serializers.SerializerMethodField()
    likes_n = LikesSerializer(many = True, read_only = True)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'content',
            'image',
            'category',
            'publish_date',
            'author',
            'status',
            'slug',
            'comments',
            'category_name',
            'likes',
            # 'post_views',  # blogun görüntülenme sayısı
            'comment_count',
            'likes_n',  # likes false olduğunda bu kısım gözükmemeli
        )

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj.id).count()

    def get_category_name(self, obj):
        return Category.objects.get(name=obj.category).name

    def get_likes(self, obj):
        return Likes.objects.filter(likes=True, post_id=obj.id).count()

