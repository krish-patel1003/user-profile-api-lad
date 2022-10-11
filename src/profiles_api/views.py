from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
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
            message = f'Hello {name}'

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