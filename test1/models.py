from django.db import models
from test2.models import Post


class Comment(models.Model):
    comment = models.TextField()
    post_comm = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return self.comment
