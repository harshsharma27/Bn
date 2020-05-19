from django.db import models


# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    Description = models.TextField()
    photo = models.ImageField(upload_to='cars')

    def __str__(self):
        return 'Author Name ' + self.name + ' - ' + self.email
