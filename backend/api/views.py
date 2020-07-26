<<<<<<< HEAD
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    permission_classes = [AllowAny]
    queryset            = Message.objects.all()
    serializer_class    = MessageSerializer
=======
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


>>>>>>> eaf6b721a7d15e744899e59f9f558cdb1de72ff1
