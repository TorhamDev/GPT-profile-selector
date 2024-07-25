from users.models import User
from rest_framework import serializers


# Note: you can add more user fields like first_name, last_name, email or etc.
# but for now this fields are good


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "gpt_api_key", "is_staff")


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = ("username", "password", "confirm_password")


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "gpt_api_key")
