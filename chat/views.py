from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from rest_framework.decorators import action
from .forms import UserRegistrationForm
from .models import User, ChatRoom, Message
from rest_framework import viewsets
from django.db import DatabaseError
from .serializers import MessageSerializers

class UserRegistrationViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post', 'get'])
    def signup(self, request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()  # Create a new user
                return redirect('login')
        else:
            form = UserRegistrationForm()  # Display empty form for GET request
        return render(request, 'signup.html', {'form': form})

    @action(detail=False, methods=['post', 'get'])
    def login(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')
            else:
                return HttpResponseBadRequest('Invalid login credentials')
        return render(request, 'login.html')

class ChatRoomViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def create_room(self, request):
        username = request.POST.get('username')
        if not username:
            return HttpResponseBadRequest("Invalid username")
        user = get_object_or_404(User, username=username)
        room_name = request.POST.get('room_name')
        if not room_name:
            return HttpResponseBadRequest("Invalid room name")
        try:
            room, created = ChatRoom.objects.get_or_create(name=room_name)
            if created:
                room.members.add(user)
        except DatabaseError as e:
            return HttpResponseBadRequest(f'Database error: {e}')
        
        return redirect('chat-retrieve_chat', room_name=room_name, username=username)

class ChatViewSet(viewsets.ViewSet):

    @action(detail=True, methods=['get'])
    def retrieve_chat(self, request, room_name=None, username=None):
        room = get_object_or_404(ChatRoom, name=room_name)
        user = get_object_or_404(User, username=username)
        messages = Message.objects.filter(chat_room=room).select_related('sender').order_by('time_stamp')
        message_serialized = MessageSerializers(messages, many=True, context={'request': request})
        context = {
            "messages": message_serialized.data,
            "room": room,
            "user": user, 
        }
        return render(request, 'room.html', context)
      
    @action(detail=True, methods=['post'])
    def create_message(self, request, room_name=None, username=None):
        room = get_object_or_404(ChatRoom, name=room_name)
        user = get_object_or_404(User, username=username)
        message_content = request.POST.get('message')

        if not message_content:
            return HttpResponseBadRequest("Message is required")
        
        try:
            message_saved = Message.objects.create(chat_room=room, sender=user, message=message_content)
        except DatabaseError as e:
            return HttpResponseBadRequest(f'Database error: {e}')    
        
        if message_saved is None:
            return HttpResponseBadRequest("Message not saved")

        messages = Message.objects.filter(chat_room=room).select_related('sender').order_by('time_stamp')
        message_serialized = MessageSerializers(messages, many=True, context={'request': request})
        context = {
            "messages": message_serialized.data,
            "room": room,
            "user": user, 
        }
        return render(request, 'chatroom.html', context)

def home(request):
     return render(request, 'chatroom.html')