from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_post', default=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))


class User(models.Model):
    pass
