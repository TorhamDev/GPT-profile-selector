from users_media.models import Images
from rest_framework import serializers


class AddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("user", "image")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"
