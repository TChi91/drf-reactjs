from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from backend.api.views import index_view, MessageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    path('', index_view, name='index'),
    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
