from django.db import models


class Announcement(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    content = models.TextField()
    summary = models.CharField(
        max_length=280
    )
    date = models.DateField(auto_now_add=True)
