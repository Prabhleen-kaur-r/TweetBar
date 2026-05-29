from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name="tweet_likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="tweet_dislikes", blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return f"{self.user} - {self.text[:20]}"