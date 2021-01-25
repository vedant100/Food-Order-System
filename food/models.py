from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=1000, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg")

def get_absolute_urls(self):
    return reverse("food:detail", kwargs={'pk', self.pk})
