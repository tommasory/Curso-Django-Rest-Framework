from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class InformationApiView(APIView):
    """ API View de Prueba """

    serializer_class = serializers.InformationSerializer

    def get(self, request, format=None):
        ''' Retornar lista de caracterisitcas del ApiView '''
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicación',
            'Esta mapeado manualmente a los URLS'
        ]

        return Response({
                'message':'Hi i am a ApiView',
                'an_apiview':an_apiview
            })

    def post(self, request):
        """ Crea un mensaje con nuestro nombre. """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message':message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



