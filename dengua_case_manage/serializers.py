from .models import DenguaCase
from rest_framework import serializers
from .models import User
class DenguaCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DenguaCase
        fields = '__all__'
    # def validate(self, data):
    #     # Extract the username from the validated data

        
    #     # Return the validated data with the created_by field set
    #     return data

    # def create(self, validated_data):
    #     # Create and return the instance using the validated data
    #     return super().create(validated_data)