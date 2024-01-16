# hotel_app/api/serializers.py
from rest_framework import serializers
from hmsAPI_app.models import UserDetails

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'
