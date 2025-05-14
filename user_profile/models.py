from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='images/')
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.bio[:20]
