from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')
router.register('comment', CommentViewSet, basename='comment')
router.register('reply', ReplyViewSet, basename='reply')

urlpatterns = [
    path('', include(router.urls)),
]
