from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from .forms import UserRegistrationForm

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

def home(request):
    return render(request, 'index.html')