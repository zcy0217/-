from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User




# Create your models here.
class Preference(models.Model):
    fk1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50)
    choice4 = models.CharField(max_length=50, default="室內")

class Preference_food(models.Model):
    fk2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    choice5 = models.CharField(max_length=50)  
    choice6 = models.CharField(max_length=50)  

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)  # 新增行程名稱欄位
    locations = models.TextField()  # 這裡存儲地點信息，可以根據實際需求調整
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   
    def __str__(self):
        return self.title