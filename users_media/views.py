from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions
from rest_framework.response import Response
from users_media.serializers import AddImageSerializer, ImageSerializer
from users_media.models import Images


class UserAddImageView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Note: it's better to check media type and size when you saving a media like an image
        # but i don't have time for it :) 
        self.request.data["user"] = self.request.user.pk
        serializer = AddImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_image = serializer.save()
        return Response(ImageSerializer(instance=user_image, context={"request":request}).data)
    
    def get(self, request):
        user_images = Images.objects.filter(user=request.user)
        return Response(ImageSerializer(instance=user_images, many=True, context={"request":request}).data)
    
