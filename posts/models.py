from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    # rate = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

