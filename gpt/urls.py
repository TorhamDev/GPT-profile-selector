from gpt.views import AskGPTForProfileView
from django.urls import path

urlpatterns = [
    path("ask-profile/", AskGPTForProfileView.as_view(), name="user_images"),
]
