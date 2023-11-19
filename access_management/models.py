from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=8)
    nickname = models.CharField(max_length=100)
    unique_token = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=10, default='USER')
    
    def __str__(self):
        return self.email