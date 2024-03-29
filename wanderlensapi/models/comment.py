from django.db import models
from .user import User
from .post import Post

class Comment(models.Model):
    """Model for the comment table"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
