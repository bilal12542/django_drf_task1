from rest_framework import serializers
from .models import Posts
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Posts.objects.all())

    class Meta:
        model = Posts
        fields = ['id', 'title', 'description', 'author']

    # def create(self, validated_data):
    #     return Posts.objects.create(**validated_data)
