from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from users.serializers import UserSerializer, UserRegisterSerializer, UserUpdateSerializer
from users.models import User
from django.shortcuts import get_object_or_404



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
            UserSerializer(instance=user).data,
            status=status.HTTP_201_CREATED,
        )
    

class UserUpdateView(APIView):
    def put(self, request, userpk):

        user = get_object_or_404(User, pk=userpk)

        serializer = UserUpdateSerializer(instance=user, data=request.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save(update_fields=["username", "gpt_api_key"])
        

        return Response(
            UserSerializer(instance=user).data,
            status=status.HTTP_201_CREATED,
        )
    
    def delete(self, request):
        # Note: You can add other methods like this
        ...