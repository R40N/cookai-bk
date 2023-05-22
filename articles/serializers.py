from rest_framework import serializers
from .models import Article, Comment, Like, Tag


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'date_posted',
                  'author', 'comments', 'likes', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'text', 'date_posted', 'author']
