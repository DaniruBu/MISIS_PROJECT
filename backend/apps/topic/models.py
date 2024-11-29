from django.db import models
from user.models import User


class Category(models.Model):
    title = models.CharField(max_length=32, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=True)
    description = models.TextField(max_length=128, blank=False)
    type_topic = models.ForeignKey(Category, on_delete=models.SET_NULL)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
