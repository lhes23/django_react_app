from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:id>', getSinglePost, name="posts"),
    path('', getAllPosts, name="posts"),
]
