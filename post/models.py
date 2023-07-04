from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=)
    caption = models.CharField()
    slug = models.CharField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.slug} - {self.updated_date}'