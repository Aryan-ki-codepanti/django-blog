from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=400 , default="")
    author = models.CharField(max_length=200)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"