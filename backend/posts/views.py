from os import stat
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

@api_view(["GET", "POST"])
def getAllPosts(request):
    match request.method:
        case "GET":
            posts = Post.objects.all()
            serializer = PostSerializer(posts,many=True)
            return Response({"posts":serializer.data})
        case "POST":
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success":serializer.data},status=status.HTTP_201_CREATED)
            return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)