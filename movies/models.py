from django.db import models
from django.utils import timezone

class Movie(models.Model):
    director = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    synopsi = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    premiere_date = models.DateTimeField(blank=True, null=True)

    def premiere(self):
        self.premiere_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title