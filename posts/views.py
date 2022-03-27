from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Posts
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your views here.

class PostCRUD(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def list(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = Posts.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        post = Posts.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        # print(help(get_user_model()))
        # print('print', help(settings.AUTH_USER_MODEL))
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
