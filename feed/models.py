from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-updated']),
        ]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('feed:detail_post', kwargs={'post_id': self.pk})


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='comment_like', blank=True)

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-updated']),
        ]

    def __str__(self) -> str:
        return self.content
