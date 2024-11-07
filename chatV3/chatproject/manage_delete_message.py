import os
import django

# Setup Django environment (update 'myproject.settings' with your actual settings module path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')
django.setup()

from chatapp.models import Message

count, _ = Message.objects.all().delete()
print(f"Deleted {count} messages.")
