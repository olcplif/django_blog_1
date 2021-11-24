from django.contrib import admin
from django.urls import path

from .views import PostViewSet, UserAPIView, PostList, PostDetailView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('posts', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('posts/<str:pk>', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    # path('user', UserAPIView.as_view()),
    path('', PostList.as_view(), name="home"),
    path('<slug:slug>/', PostDetailView.as_view(), name="post-detail"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]

