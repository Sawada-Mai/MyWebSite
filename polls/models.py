from django.db import models
from django.utils import timezone

# Create your models here

class Album(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField("image", upload_to='photo/')
    add_date = models.DateField("registration date", auto_now_add=True)
    explanation = models.TextField()

    def __str__(self):
        return self.title

class  Portfolio(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField("image", upload_to='portfolio/')
    detail = models.CharField(max_length=50)
    date = models.DateField("date",default=timezone.now)
    text1 = models.TextField()
    text2 = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField("date")
