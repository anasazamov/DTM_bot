from django.db import models

# Create your models here.

class Users(models.Model):
    
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    chat_id = models.IntegerField()
