from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(validators=[])

    class Meta:
        model = User
        fields = ['email', 'active', 'id']
        extra_kwargs = {
            'id': {'validators': []}
        }

    def create(self, validated_data):
        obj, _ = User.objects.update_or_create(defaults={"active":True}, id=validated_data['id'])
        return obj

class UserUnsubSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']
        extra_kwargs = {
            'id': {'validators': []}
        }

    def create(self, validated_data):
        obj, _ = User.objects.update_or_create(defaults={"active":True}, id=validated_data['id'])
        return obj
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']