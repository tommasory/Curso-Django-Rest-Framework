from rest_framework import serializers

class InformationSerializer(serializers.Serializer):
    """ Serializar un campo para nuestro APIView """
    name = serializers.CharField(max_length=10)
    

