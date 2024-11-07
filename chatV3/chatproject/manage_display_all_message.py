import os
import django

# Setup Django environment (update 'myproject.settings' with your actual settings module path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')
django.setup()

from chatapp.models import Message

messages = Message.objects.all()
if messages.exists():
    for message in messages:
        print(f"{message.timestamp} - From {message.sender} to {message.receiver}: {message.content}")
else:
    print("No messages found.")
