from django.db import models

# Create your models here.
class Media(models.Model):
    heading = models.TextField(max_length=250)
    images = models.ImageField(upload_to='photos/',blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to='videos/')
    date_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.heading[:50]
