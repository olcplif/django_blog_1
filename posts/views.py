import random

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.views import generic
from django.views.generic import ListView, CreateView

from .models import Post, User
from .serializers import PostSerializer


class PostViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/posts
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/posts
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/posts/<str:id>
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/posts/<str:id>
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/posts/<str:id>
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'


# class HomeView(ListView):
#     model = Post
#     template_name = 'index.html'
#     context_object_name = 'posts'


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
