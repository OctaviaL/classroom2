from django.db import models

class Comment(models.Model):
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment
