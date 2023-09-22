from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurants.models import Menu


class Employee(AbstractUser):
    position = models.CharField(max_length=255)
    votes = models.ForeignKey(
        to=Menu, related_name="employees", on_delete=models.DO_NOTHING, null=True, blank=True
    )
