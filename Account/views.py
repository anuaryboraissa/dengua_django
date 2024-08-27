from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

from .serializer import UserSerializer,PasswordResetSerializer,CustomTokenObtainPairSerializer,PasswordChangeSerializer
# Create your views here.
class ObtainTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class PasswordChangeView(APIView):
    serializer_class = PasswordChangeSerializer
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password change successfully.","status":status.HTTP_200_OK})

class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password reset successfully.", "status":status.HTTP_200_OK})
    
class UserManagementView(APIView):
    def post(self,request):
         try:
            serializer = UserSerializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                user_data = serializer.data
                auth_user = get_user_model()
                user=auth_user.objects.create_user(**user_data)
                access_token,refreshToken=create_user_and_generate_token(user)
                data=serializer.data
                data.pop('password', None)
                return Response({"data":data, "status":status.HTTP_200_OK,"token":{"access":access_token,"refresh":refreshToken}})
            errors=extract_error_messages(serializer.errors)
            return Response({"data":errors, "status":status.HTTP_404_NOT_FOUND,"access":None})
         except Exception as e:
             return Response({"data":f"{e}", "status":status.HTTP_404_NOT_FOUND,"access":None})
    def get(self,request):
        username = request.GET.get('username')
        if username is not None:
            user=User.objects.filter(username=username)
            if user.exists():
               serializer=UserSerializer(user[0])
               data=serializer.data
               data.pop('password', None)
            return Response({"message":"success","data":data,"status":status.HTTP_200_OK})
        else:
            return Response({"message":"success","data":None,"status":status.HTTP_200_OK})  
        
    def put(self,request):
        data=request.data
        user=User.objects.get(username=data['username'])
        user.__dict__.update(**data)
        user.save()
        serializer=UserSerializer(user)
        data=serializer.data
        data.pop('password', None)
        return Response({"message":"success","data":data,"status":status.HTTP_200_OK})

def create_user_and_generate_token(user):
    # Generate JWT token
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return access_token,refresh_token

def extract_error_messages(errors):
    messages = []
    if isinstance(errors, dict):
        for key, value in errors.items():
            messages.extend(extract_error_messages(value))
    elif isinstance(errors, list):
        for error in errors:
            messages.append(str(error))
    return messages