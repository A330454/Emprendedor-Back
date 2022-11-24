from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=80, min_length=1, required=True)
    password=serializers.CharField(max_length=80, min_length=1, required=True)

    def validate(self,data):
        user = authenticate(username= data['username'], password = data['password'])
        if not user:
            raise serializers.ValidationError({status.HTTP_403_FORBIDDEN:'Usuario o Contraseña Invalida'})
        self.context['user'] = user
        return data
    
    def create(self, data):
        user = self.context['user']
        token, created = Token.objects.get_or_create(user=user)
        return {
            'user':user.username,
            'token':token.key,
            'info':user.id,
            'admin':user.is_superuser == True
        }