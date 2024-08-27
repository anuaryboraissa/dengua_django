from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    # def to_representation(self, instance):
    #         representation = super().to_representation(instance)
    #         request = self.context.get('request')
    #         print(f"method: {request}")
    #         if request and request.method in ['GET', 'PUT', 'PATCH']:  # Exclude password in non-authentication scenarios
    #           representation.pop('password', None)
    #         return representation
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user'] = user.username
        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        user=UserSerializer(self.user)
        user_data=user.data
        user_data.pop("password")
        user_data.pop("is_superuser")
        data["user"]=user_data
        return data
    
class PasswordChangeSerializer(serializers.Serializer):
    username = serializers.CharField()
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"errors":["User not found."]})
        
        # Check if the old password matches the user's current password
        if not check_password(old_password, user.password):
            raise serializers.ValidationError({"errors":["Incorrect old password."]})
        
        # Check if the new password matches the confirmation
        if new_password != confirm_password:
            raise serializers.ValidationError({"errors":["Password do not match."]})
        if not any(char.isupper() for char in new_password) or  len(new_password) < 8:
             raise serializers.ValidationError({"errors":["Password must be atleast 8 length with atleast one upper case letter."]})
        return data

    def save(self):
        username = self.validated_data['username']
        new_password = self.validated_data['new_password']
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)  # This method hashes the password
            user.save()
        except User.DoesNotExist:
            raise serializers.ValidationError({"errors":["User not found."]})
class PasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"errors":["Passwords do not match."]})
        if not any(char.isupper() for char in data['new_password']) or  len(data['new_password']) < 8:
             raise serializers.ValidationError({"errors":["Password must be atleast 8 length with atleast one upper case letter."]})
        return data

    def save(self):
        username = self.validated_data['username']
        new_password = self.validated_data['new_password']
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)  # This method hashes the password
            user.save()
        except User.DoesNotExist:
            raise serializers.ValidationError({"errors":["User not found."]})
        