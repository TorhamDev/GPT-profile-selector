from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from gpt.serializers import AddImageSerializer
from users_media.serializers import ImageSerializer
from users_media.models import Images
from gpt.utils import ask_gpt_about_profile


class AskGPTForProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AddImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_images = Images.objects.filter(
            pk__in=serializer.validated_data["image_ids"], user__pk=request.user.pk
        )

        gpt_answer = ask_gpt_about_profile(
            api_key=request.user.gpt_api_key,
            username=request.user.username,
            user_images=user_images,
        )
        print(gpt_answer)

        return Response(
            {
                "selected_image": ImageSerializer(
                    instance=user_images[gpt_answer["image"]-1],
                    context={"request": request},
                ).data,
                "reason": gpt_answer["reason"],
            }
        )
