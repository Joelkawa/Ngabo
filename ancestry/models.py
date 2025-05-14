from django.db import models

# Create your models here.
class Origin(models.Model):
    origin = models.TextField()
    last_updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Our Origin {self.origin[:20]}'
