from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    
    User_Type_Choices = [
        ("advertise", "Advertise"),
        ("influencer", "Influencer"),
    ]
    user_choice = models.CharField(choices=User_Type_Choices, default="influencer", max_length=200)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", null=True)
    
    
    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True
    )
    

class Influencer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="influencer")
    description = models.TextField(blank=True)
    followers = models.PositiveIntegerField(default=0)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

 
class Advertise(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="advertise")
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    influencers = models.ManyToManyField(Influencer, related_name="advertise")
   
    
    def __str__(self):
        return self.company
