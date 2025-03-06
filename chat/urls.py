from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserRegistrationViewSet, ChatRoomViewSet, ChatViewSet, home

router = DefaultRouter()
router.register(r'registration', UserRegistrationViewSet, basename='user')
router.register(r'chatRoom', ChatRoomViewSet, basename='chatRoom')
router.register(r'chat', ChatViewSet, basename='chat')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home, name='home'),
    path('login/', UserRegistrationViewSet.as_view({'get': 'login', 'post': 'login'}), name='login'),
    path('chatRoom/create/', ChatRoomViewSet.as_view({'post': 'create_room'}), name='chatRoom-create_room'),
    path('chat/<str:room_name>/<str:username>/', ChatViewSet.as_view({'get': 'retrieve_chat'}), name='chat-retrieve_chat'),
]