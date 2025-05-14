from django.db import models
from django.conf import settings



# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='recieved_messages', on_delete=models.CASCADE)
    contents = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    #audio = models.FileField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return f'{self.sender} to {self.recipient}: {self.contents[:20]} '
    

