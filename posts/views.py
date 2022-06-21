from django.shortcuts import render
from django.contrib.auth import get_user_model # new
from rest_framework import viewsets # new

# Create your views here.
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly # new
from .models import Post
#from .serializers import PostSerializer
from .serializers import PostSerializer, UserSerializer # new

#class PostList(generics.ListCreateAPIView):

    # queryset = Post.objects.all()
     #serializer_class = PostSerializer

#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = (permissions.IsAuthenticated,) # new
    #permission_classes = (IsAuthorOrReadOnly,) # new
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer

#class UserList(generics.ListCreateAPIView): # new

     #queryset = get_user_model().objects.all()
     #serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new

    # queryset = get_user_model().objects.all()
    # serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet): # new
     permission_classes = (IsAuthorOrReadOnly,)
     queryset = Post.objects.all()
     serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): # new
     queryset = get_user_model().objects.all()
     serializer_class = UserSerializer