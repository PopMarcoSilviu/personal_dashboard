from django.contrib.auth import authenticate
from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User


class PersonalDashboardView(APIView):

    def get(self, format=None):
        return Response({'letter': 'a'})


class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = (AllowAny,)

    # def get(self, format=None):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # def put(self, request):
    #
    #     serializer = UserSerializer(data=request.data).initial_data
    #     user = authenticate(username=serializer['username'], password=serializer['password'])
    #
    #     if user is not None:
    #         return Response(
    #             {},
    #             status=status.HTTP_202_ACCEPTED
    #         )
    #     else:
    #         return Response(
    #             {},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )

# Create your views here.
