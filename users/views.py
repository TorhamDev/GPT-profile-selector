from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from users.serializers import UserSerializer, UserRegisterSerializer
from django.contrib.auth.models import User



class UserRegisterView(APIView):
    def post(self, request):
        
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["password"] != serializer.validated_data["confirm_password"]:
            raise ValidationError
        
        user = User(username=serializer.validated_data["username"])
        user.set_password(serializer.validated_data["password"])
        user.save()

        return Response(
            UserSerializer(instance=user, context={'request': request}).data,
            status=status.HTTP_201_CREATED,
        )