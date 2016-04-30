

from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Blog, Comment
from .serializers import UserSerializer, BlogSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    model = Blog
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_class = [TemplateHTMLRenderer]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request):
    	self.object = self.get_object()
    	return Response({'blogs': self.object}, template_name='blogs/index.html')


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    """
    def get_queryset(self):
    	self.blog = self.kwargs['blog_id']

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user, blog=self.blog)"""