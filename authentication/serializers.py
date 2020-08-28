from rest_framework import serializers
from users.serializers import UserSerializer
from rest_auth.models import TokenModel

#SERIALIZER QUE ME DEVUELVE EL TOKEN, PERO TAMBIEN LOS DATOS DEL USUARIO ACTUAL
#AL MOMENTO DE HACER LOGIN Y EL REGISTRO
#---TOCA SELECCIONARLO EN SETTINGS---
class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)  
    class Meta:
        model = TokenModel
        fields = ('key', 'user') 