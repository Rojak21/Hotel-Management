# hotel_app/api/urls.py
from django.urls import path

from hmsAPI_app.api.views import api_example, login_api, register_api
# from .views import UserProfileDetailAPIView

urlpatterns = [
    # path('user-profile/', UserProfileDetailAPIView.as_view(), name='user-profile-detail'),
    path('api-example/', api_example, name='api-example'),
    path('register/', register_api, name='register-api'),
    path('login/', login_api, name='login-api'),
]
