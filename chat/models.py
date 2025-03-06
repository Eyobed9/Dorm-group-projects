
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.core.exceptions import ValidationError


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True)
    is_influencer  = models.BooleanField(default=False)
    is_advertiser = models.BooleanField(default=False, null=False)

class Influencer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='influencer')
    description = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)


class Advertiser(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='advertiser')
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    website = models.URLField(blank=True, null=True)
    #company

class Rate(models.Model):
    Influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name='rates')
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatRoom(models.Model):
    name = models.CharField(max_length=250)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chat_rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    # is_private = models.BooleanField(default=False)
    # is_group = models.BooleanField(default=False)

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='sender')
    time_stamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    image = models.ImageField(upload_to='chat/images/', blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username + ' ' + self.message if self.sender else 'Unknown User'
    
    def clean(self):
        if not self.message and not self.image:
            raise ValidationError('Message or image is required')
        
     # Validation: The full_clean method ensures that the instance is valid before saving it to the database.   
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

       


    

  
    
  
    



 


