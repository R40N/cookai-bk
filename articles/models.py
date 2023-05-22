from django.db import models
from django.utils import timezone
from users.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return self.author.nickname


class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.name
