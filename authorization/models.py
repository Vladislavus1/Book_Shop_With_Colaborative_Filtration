from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class CustomUser(AbstractUser):
    search_history = ArrayField(models.CharField(default=""), default=list)
    views_history = ArrayField(models.CharField(default=""), default=list)
    favorite_books = ArrayField(models.IntegerField(default=0), default=list)
    detectives_count = models.IntegerField(default=0)
    fighters_count = models.IntegerField(default=0)
    romantics_count = models.IntegerField(default=0)
    fantasy_count = models.IntegerField(default=0)
    thrillers_count = models.IntegerField(default=0)

    def add_view_log(self, book_id):
        self.views_history.append(book_id)
        self.save()

    def __str__(self):
        return self.username
