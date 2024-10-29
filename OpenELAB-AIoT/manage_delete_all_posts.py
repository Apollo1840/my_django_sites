import os
import django

# Setup Django environment (update 'myproject.settings' with your actual settings module path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# Import the Post model (update 'myapp' with the actual app name where your Post model resides)
from blog.models import Post
import json

# Delete all existing posts
Post.objects.all().delete()
print("All existing posts have been deleted.")
