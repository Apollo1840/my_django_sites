# chatapp/views.py

from django.shortcuts import render, redirect
from .models import Message


def chat_view(request, user_id):
    user_id = int(user_id)
    other_user_id = 2 if user_id == 1 else 1

    if request.method == 'POST':
        text = request.POST.get('message')
        if text:
            Message.objects.create(sender=user_id, recipient=other_user_id, text=text)
        return redirect(f'/chat/{user_id}')

    messages = Message.objects.filter(
        sender__in=[user_id, other_user_id],
        recipient__in=[user_id, other_user_id]
    )
    return render(request, 'chatapp/chat.html', {'messages': messages, 'user_id': user_id})
