from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hms_app.urls')),
    # path('account/', include('django.contrib.auth.urls')),  # Use built-in views for login, logout, and password reset
]
