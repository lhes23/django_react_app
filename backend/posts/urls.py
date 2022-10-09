from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',PostViewSet)

urlpatterns = [
    # path('<int:id>', getSinglePost, name="posts"),
    # path('', getAllPosts, name="posts"),
    path("",include(router.urls))
]
