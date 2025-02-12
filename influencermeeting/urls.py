from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    
]
if settings.DEBUG:  # Only load Debug Toolbar in DEBUG mode
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
