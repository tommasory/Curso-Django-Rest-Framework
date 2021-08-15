from rest_framework.views import APIView
from rest_framework.response import Response

class InformationApiView(APIView):
    """ API View de Prueba """

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
