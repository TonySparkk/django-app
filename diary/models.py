from django.db import models

# Create your models here.
class Post(models.Model):
    AUTHOR = (
        ('O', 'Orgest'),
        ('E', 'Eduina'),
    )
    author = models.CharField(max_length=1, choices=AUTHOR)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.title
