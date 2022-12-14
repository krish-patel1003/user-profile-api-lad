from django import views
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import (
    HelloSerializer,
    ProfileFeedItemSerializer,
    UserProfileSerializer,
)
from .models import ProfileFeedItem, UserProfile
from .permissions import PostOwnStatus, UpdateOwnProfile
# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""
    
    serializer = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'users HTTP methos ad fucntion (get, post, path, put, delte)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': "Hello world!", 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello message with our name"""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}, from APIView'

            return Response({'mesage': message})

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided int he request"""

        return Response({"method":"patch"})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({"mehtod":"delete"})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return Hello message"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Providers more functionality with less code',
        ]

        return Response({"message": "Hello", "a_viewset":a_viewset})
    
    def create(self, request):
        """Create a new Hello message"""
        serializer = HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}, from ViewSet'

            return Response({"message":message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Handles getting ana object by its ID"""

        return Response({"http_method":"GET"})
    
    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({"http_method":"PUT"})   

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({"http_method":"PATCH"})
    
    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({"http_method":"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles reading, creating, and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and reurns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken to validate and create a token"""

        return ObtainAuthToken().as_view()(request=request._request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed item"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    # permission_classes = (PostOwnStatus, IsAuthenticatedOrReadOnly,)
    permission_classes = (PostOwnStatus, IsAuthenticated,)

    def create(self, request):
        """Creates new Feed"""
        serializer = self.get_serializer(data=request.data)
        print('request user - ', request.user)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    # def perfom_create(self, serializer):
    #     """Sets user profile to the logged in user"""
    #     print("request.user - ",self.request)
    #     serializer.save(user=self.request.user)

