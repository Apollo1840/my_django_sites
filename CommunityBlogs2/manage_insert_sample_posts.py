import os
import django

# Setup Django environment (update 'myproject.settings' with your actual settings module path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# Import the Post model (update 'myapp' with the actual app name where your Post model resides)
from blog.models import Post
from django.contrib.auth.models import User

user = User.objects.first()

# Create post data
posts_data = [
    {
        "author": user,
        "title": "Travel Diary 2",
        "content": "Exploring Europe",
    },
    {
        "author": user,
        "title": "Tech Thoughts 2",
        "content": "Introduction to AI",
    },
    {
        "author": user,
        "title": "Recipe Corner 2",
        "content": "Delicious Vegan Dishes",
    }
]

# Insert posts into the database
for post_data in posts_data:
    post = Post(
        author=post_data["author"],
        title=post_data["title"],
        content=post_data["content"],
    )
    post.save()
    print(f'Inserted post: {post.title} by {post.author}')

print("All posts inserted successfully!")
