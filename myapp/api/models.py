from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.task 
