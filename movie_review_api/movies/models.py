from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    # You can extend the user model if needed
    pass

class Review(models.Model):
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 rating
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie_title} - {self.user.username}'