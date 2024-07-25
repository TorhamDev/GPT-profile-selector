from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gpt_api_key = models.CharField(
        max_length=70, help_text="User chatGPT API key.", null=True, blank=True
    )
