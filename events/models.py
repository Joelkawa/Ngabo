from django.db import models
from django.conf import settings

# Create your models here.
class FamilyEvents(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/',blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    happening_date = models.DateTimeField()

    def __str__(self):
        return self.name
