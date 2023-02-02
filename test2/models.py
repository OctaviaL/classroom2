from django.db import models


class Post(models.Model):
    post = models.TextField()

    
    def __str__(self) -> str:
        return self.post

