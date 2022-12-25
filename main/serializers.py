from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def update(self, instance, validated_data, email):
        instance  = User.objects.get(email=email)
        instance.active = validated_data.get("False", instance.active)
        return super().update(instance, validated_data)
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']