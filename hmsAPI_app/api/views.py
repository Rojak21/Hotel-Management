from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hmsAPI_app.models import UserDetails
from .serializers import UserProfileSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def api_example(request):
    data = {'message': 'Hello, this is an API endpoint!'}
    return JsonResponse(data)

@csrf_exempt
@api_view(['POST'])
def register_api(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        user_data = serializer.validated_data

        # Create User object
        user = User.objects.create_user(
            username=user_data['emailid'],
            email=user_data['emailid'],
            password=user_data['password']
        )

        # Create UserDetails object
        UserDetails.objects.create(
            user=user,
            fullname=user_data['fullname'],
            emailid=user_data['emailid'],
            password=user_data['password']
        )

        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_api(request):
    email = request.data.get('emailid')
    password = request.data.get('password')

    try:
        user_details = UserDetails.objects.get(emailid=email, password=password)
    except UserDetails.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'message': 'Login successful'})