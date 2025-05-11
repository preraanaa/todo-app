from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

