from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateUserSerializers, LoginSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
import logging
from rest_framework.exceptions import PermissionDenied

logger = logging.getLogger(__name__)


# @permission_classes((IsAuthenticated,))
class UserAction(APIView):
    def post(self, request):
        try:
            request_data = request.data
            # Instance of model
            serialized_data = CreateUserSerializers(data=request_data)
            if serialized_data.is_valid():
                check_user = User.objects.filter(username=request_data['username'])
                if check_user.exists():
                    response = {
                        'message': 'User Already Exists',
                        'data': serialized_data.data
                    }
                else:
                    serialized_data.save()
                    response = {
                        'message': 'User Added Successfully',
                        'data': serialized_data.data
                    }
                return Response(response, status.HTTP_201_CREATED)
            else:
                return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return PermissionDenied
            # return Response(e, status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        # after successfull validation in serializer, a validated data dict will be attached to serializer
        if serializer.is_valid():
            # to get that attached validated data dict
            user = serializer.validated_data['user']
            django_login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": serializer.errors}, status=404)
