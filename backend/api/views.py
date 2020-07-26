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
