from django.contrib.auth.models import User
from django.db import models
from django.db.models.expressions import F
from django.utils.timezone import now

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

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , null=True)
    timeStamp = models.DateTimeField(default=now)
    # parent

    def __str__(self):
        return f"{self.comment} by {self.user.username} on {self.post.title[0:20]}..."
