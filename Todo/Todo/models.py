from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=70, blank=False, null=True)
    description = models.TextField(max_length=350)
    is_done = models.BooleanField()

    def __str__(self):
        return self.title
