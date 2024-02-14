from django.db import models
class Shop(models.Model):
 sname=models.CharField(max_length=100)
 p=models.TextField(default='')
 sid=models.CharField(max_length=1000)
 address=models.TextField(default='none')
 def __str__(self):
  return self.sid
# Create your models here.
