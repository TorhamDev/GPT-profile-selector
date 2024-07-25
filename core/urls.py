from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


api_v1_urls = [
    path("users/", include("users.urls"), name="users"),
    path("media/", include("users_media.urls"), name="user_meida"),
    path("gpt/", include("gpt.urls"), name="gpt_apis"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_urls), name="api_v1"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Note: We can make versioning better maybe by adding another list variable like 'APIs' then and version into it
# but this is a simple project and for versioning I like to change project structure and handle versioning in the structure itself
