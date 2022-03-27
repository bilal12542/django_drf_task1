from rest_framework import serializers
from .models import MyUser
from posts.models import Posts


class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, queryset=Posts.objects.all())
    # email_r = serializers.ReadOnlyField(source='email')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'full_name', 'post', 'owner']
