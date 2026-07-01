from django.contrib.auth import get_user_model
from .serializers import SignUpSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

User = get_user_model()


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)

            response = {
                "message": "Login successful",
                "token": token.key
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response(
            {"message": "Invalid email or password"},
            status=status.HTTP_400_BAD_REQUEST
        )