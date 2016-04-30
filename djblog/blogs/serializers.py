
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Blog, Comment


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'}
                                     )

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser',
                            'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Blog
        fields = ('url', 'title', 'text', 'owner')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    blog = serializers.ReadOnlyField(source='blog.title')

    class Meta:
        models = Comment
        fields = ('url', 'text', 'owner', 'blog')
