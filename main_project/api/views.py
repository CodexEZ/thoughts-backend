from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostsSerializer, PostsCreateSerializer, CreateUserSerializer, UserLoginSerializer
from api.models import Posts, Users
# Create your views here.

@api_view(['GET'])
def getPosts(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    serializer = PostsCreateSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.data['title'])
        q = Users.objects.get(pk = serializer.data['user'])
        q.posts_set.create(title = serializer.data['title'],desc = serializer.data['desc'])
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = CreateUserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def userLogin(request):
    serializer = UserLoginSerializer(data = request.data)
    print(request.data)
    if serializer.is_valid():
        q = Users.objects.get(pk = serializer.data['username'])
        print("Valid")
        if q.password == serializer.data['password']:
            return Response(serializer.data)
    else:
        print(serializer.errors)
    return Response()
