from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title