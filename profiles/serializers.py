from django.db.models import fields
from rest_framework import serializers

from . import models

class InformationSerializer(serializers.Serializer):
    """ Serializar un campo para nuestro APIView """
    name = serializers.CharField(max_length=50)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """

    class Meta:
        model = models.UserProfile
        # Campos a mostrar
        fields = ('id', 'email', 'name', 'password')
        # Execiones
        extra_kwargs = {
            # Con esto protejemos la contraseña a la hora de retorno
            'password':{
                'write_only':True,# La clave se muestra solo cuando estamos creando
                'style':{'input_type', 'password'} # Mostrar asterisco y no los datos
            }
        }
    # Sobreescribimos la funcion para manterner la proteccion de la clave.
    def create(self, validated_data):
        """ Crear y retornar nuevo usuario """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


