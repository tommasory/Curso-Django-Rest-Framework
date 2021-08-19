from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from . import serializers, models, permissions

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

    def put(self, request, pk=None):
        """ Maneja actulizar un objeto """
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actulizacion parcial de un objeto """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Borrar un objeto """
        return Response({'method':'DELETE'})

class InformationViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.InformationSerializer

    def list(self, request):
        """ Retorna mensaje de Hola Mundo """

        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update)',
            'Automaticamente mapea a los URLs usando RRouters',
            'Provee mas funcionalidad con menos codigo',
        ]
        return Response({'message':'Hola !','a_viewset':a_viewset})

    def create(self, request):
        """ Crea un nuevo mensaje de hola mundo. """

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

    def retrieve(self, request, pk=None):
        """ Obtiene un Objeto y su ID """
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """ Actualiza un Objeto """
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Actualiza parcialmente el Objeto """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Destruye un Objeto """
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    # Para colocar filtro
    filter_backends = (filters.SearchFilter,)
    # Campos de busqueda
    search_fields = ('name', 'email',)





