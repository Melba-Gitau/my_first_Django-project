from ssl import Options
from django.db import models

# Create your models here.

class post(models.model):
    post=models.CharField(max_length=200)
    Text = models.CharField(max_length="textfield") 
    Author=models.ForeignKey(post,on_delete=models.CASCADE)
    Created_date=models.DateTimeField()
    Published_date=models.DateTimeField()
