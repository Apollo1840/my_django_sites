# chatapp/views.py

from django.shortcuts import render, redirect
from .models import Message
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def chat_view(request, user_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(
            sender=user_id,
            receiver=2 if user_id == 1 else 1,
            content=content
        )

        # genai.configure(api_key=GENERATIVE_AI_KEY)
        # model = genai.GenerativeModel("gemini-pro")
        # bot_response = model.generate_content(user_message)
        bot_response = content.split(" ")[-1]

        Message.objects.create(sender=0, receiver=2 if user_id == 1 else 1, content=bot_response)

        return redirect(f'/chat/{user_id}/')
    return render(request, 'chat.html', {'user_id': user_id})


def fetch_messages(request):
    messages = Message.objects.filter(
        sender__in=[0, 1, 2],
        receiver__in=[1, 2]
    ).order_by('timestamp')
    data = [
        {
            'sender': msg.sender,
            "receiver": msg.receiver,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for msg in messages
    ]
    return JsonResponse(data, safe=False)
