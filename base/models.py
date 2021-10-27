from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True , blank=True)


    def __str__(self):
        return f"{self.name} : {self.content[:50]}"