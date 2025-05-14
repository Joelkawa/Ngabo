from django.db import models
from django.contrib.auth.models import User
from django.conf import Settings,settings

# Create your models here.
# for the post
class FamilyPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



