from django.db import models
from .post import Post
from .tag import Tag

class PostTag(models.Model):
    """Model for Post Tag join table"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='posts')
