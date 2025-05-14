from django.db import models

# Create your models here.
class OurHistory(models.Model):
    subject = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    video = models.FileField(blank=True, null=True, upload_to='videos/')

    def __str__(self):
        return f"{self.subject}'s History"
