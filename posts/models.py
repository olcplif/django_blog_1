from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass
