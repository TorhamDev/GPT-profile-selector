from django.db import models
from users.models import User


class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Note: for now we dont have soft-delete
    image = models.ImageField()
