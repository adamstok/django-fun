from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Messages(models.Model):
    date = models.DateField(auto_now_add=True)
    from_mail = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f'Message from: {self.from_mail} -> {self.message} ; received: {self.date}'
    def get_delete(self):
        return f'/seemessages/{self.id}'