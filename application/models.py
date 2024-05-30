from django.db import models

# Create your models here.
class Post(models.Model):
    Nomi = models.TextField()
    Narxi = models.IntegerField()
    Rasmi = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Nomi