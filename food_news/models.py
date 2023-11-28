# cafe_news/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.title
