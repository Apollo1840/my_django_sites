from django.db import models

class Message(models.Model):
    sender = models.IntegerField()
    recipient = models.IntegerField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
