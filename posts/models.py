from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    # rate = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to="posts")    
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

