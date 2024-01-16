from atexit import register
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from .api.urls import urlpatterns as api_urls

urlpatterns = [
    # path('api/', include(api_urls)),
    path('api/', include('hmsAPI_app.api.urls')),
]