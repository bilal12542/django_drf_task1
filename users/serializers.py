from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(many=True, queryset=MyUser.objects.all())
    email_r = serializers.ReadOnlyField(source='email')
    class Meta:
        model = MyUser
        fields = ['id', 'email_r', 'full_name', 'is_admin']
