# chatapp/models.py

from django.db import models

class Message(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content}"
