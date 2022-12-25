from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
        
    def update(self, instance, validated_data):
        instance.active = validated_data.get(False, instance.active)
        instance.save()
        return instance
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']