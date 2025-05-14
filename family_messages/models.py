from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Family_Messages(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text_message = models.TextField(blank=True, null=True)
    image_message = models.ImageField(blank=True, null=True, upload_to='images/')
    video_message = models.FileField(upload_to='videos/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_message[:20]

