from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, Group, Permission
import json
# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=500)
    book_image = models.URLField(max_length=500)
    book_price = models.CharField(max_length=500)
    book_author = models.CharField(max_length=500)
    book_genre = models.CharField(max_length=500)
    book_url = models.URLField(max_length=500)
    views = ArrayField(models.IntegerField(default=0), default=list)

    def add_view(self, user_id):
        self.views.append(user_id)
        self.save()

    def __str__(self):
        return self.book_title


class Feedback(models.Model):
    author = models.ForeignKey('authorization.CustomUser', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    feedback_text = models.TextField(default="Текст відгуку відсутній")

    def __str__(self):
        return f"{self.author} - {self.stars}"