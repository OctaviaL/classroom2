from django.db import models
from test1.models import Comment

class Post(models.Model):
    post = models.TextField()
    post_comm = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return self.post

