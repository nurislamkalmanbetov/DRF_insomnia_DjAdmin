from django.db import models

# Create your models here.


"""
class Post:
    id int
    title str(50)
    content text
    created_at datetime
"""

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that when the post is created, the created_at field will be set to the current date and time

    def __str__(self) -> str:
        return self.title