from users_media.views import UserAddImageView
from django.urls import path

urlpatterns = [
    path('images/', UserAddImageView.as_view(), name="user_images"),

]
