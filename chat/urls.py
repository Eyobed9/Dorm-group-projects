from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet, home

router = DefaultRouter()
router.register(r'registration', UserRegistrationViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home, name='home'),
    path('login/', UserRegistrationViewSet.as_view({'get': 'login', 'post': 'login'}), name='login'),  # Add this line
]