from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DatosEnvio
class DatosEnvioSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatosEnvio
        fields = ('direccion', 'ciudad', 'codigo_postal')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
    
    def create(self, validated_data):
        user = User(
            username=validated_data['email'],  # Usar email como username
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user