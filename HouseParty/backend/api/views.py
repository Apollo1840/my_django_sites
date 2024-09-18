from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


"""
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("<h1> hello world! </h1>")
"""
