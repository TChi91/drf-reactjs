from django.db import models
from rest_framework import serializers

<<<<<<< HEAD
class Message(models.Model):
    subject = models.CharField(max_length=200)
    body    = models.TextField()
=======

class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')
>>>>>>> eaf6b721a7d15e744899e59f9f558cdb1de72ff1
