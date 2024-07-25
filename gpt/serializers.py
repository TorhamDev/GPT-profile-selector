from rest_framework import serializers


class AddImageSerializer(serializers.Serializer):
    image_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )
