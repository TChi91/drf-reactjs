from django.contrib import admin
from django.urls import path

from rest_framework import routers
from .views import MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = router.urls