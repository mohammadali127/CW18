from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #image filed
    password = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)

