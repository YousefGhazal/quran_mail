from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(validators=[])

    class Meta:
        model = User
        fields = ['email', 'active']
        extra_kwargs = {
            'email': {'validators': []}
        }

    def create(self, validated_data):
        obj, _ = User.objects.update_or_create(defaults={"active":True}, email=validated_data['email'])
        return obj

    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']