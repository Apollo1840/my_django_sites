# chatproject/urls.py

from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/<int:user_id>/', views.chat_view, name='chat'),
    path('fetch_messages/', views.fetch_messages, name='fetch_messages'),
]
