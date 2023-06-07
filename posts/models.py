from pickle import TRUE
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


"""
class Post:
    id int
    title str(50)
    content text
    created_at datetime
"""

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that when the post is created, the created_at field will be set to the current date and time
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts") 
    # это поле будет ссылаться на пользователя, который создал пост. on_delete=models.
    # CASCADE означает, что если пользователь будет удален, то и все его посты будут удалены

    def __str__(self) -> str:
        return self.title
    
