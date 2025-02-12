from django.contrib import admin

from .models import CustomUser, Influencer

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # You can customize the admin interface here if needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)







