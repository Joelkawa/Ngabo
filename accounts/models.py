from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    usable_password = models.BooleanField(default=True)

    def __str__(self):
        return self.username