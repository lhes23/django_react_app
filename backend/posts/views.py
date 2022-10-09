from os import stat
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

from rest_framework import viewsets

# @api_view(["GET", "POST"])
# def getAllPosts(request):
#     match request.method:
#         case "GET":
#             posts = Post.objects.all()
#             serializer = PostSerializer(posts,many=True)
#             return Response({"posts":serializer.data})
#         case "POST":
#             serializer = PostSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"success":serializer.data},status=status.HTTP_201_CREATED)
#             return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(["GET","PUT","DELETE"])
# def getSinglePost(request,id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         return Response({"errors":"No post found for id " + id},status=status.HTTP_400_BAD_REQUEST)
        
#     match request.method:
#         case "GET":
#             serializer = PostSerializer(post)
#             return Response({"post":serializer.data},status=status.HTTP_200_OK)
#         case "DELETE":
#             post.delete()
#             return Response({"status":"Post deleted!"},status=status.HTTP_202_ACCEPTED)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    