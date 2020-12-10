from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    todo = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.todo[:12]

    class Meta:
        ordering = ('-created',)