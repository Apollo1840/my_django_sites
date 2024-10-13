import os
import django

# Setup Django environment (update 'myproject.settings' with your actual settings module path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# Import the Post model (update 'myapp' with the actual app name where your Post model resides)
from blog.models import Post
import json

with open("posts.json") as f:
    posts_json = json.load(f)

# Insert posts into the database
for post_data in posts_json:
    post = Post(
        author=post_data["author"],
        title=post_data["title"],
        content=post_data["content"],
    )
    post.save()
    print(f'Inserted post: {post.title} by {post.author}')

print("All posts inserted successfully!")
