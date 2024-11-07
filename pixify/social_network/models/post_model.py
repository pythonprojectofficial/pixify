from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'posts'
