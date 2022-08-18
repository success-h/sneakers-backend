from .serializers import GoogleSocialAuthSerializer, TwitterAuthSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import  status, permissions
from .serializers import *  
from rest_framework.response import Response
from django_filters import rest_framework as filters


import environ
env = environ.Env()
environ.Env.read_env()

class UserView(APIView):
    permisson_classes = [permissions.DjangoModelPermissions]

    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)




class TwitterSocialAuthView(GenericAPIView):
    serializer_class = TwitterAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)