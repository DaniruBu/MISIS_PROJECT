from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=100, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
