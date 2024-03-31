from django.db import models

# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length = 30)

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')

class PageModel(models.Model):
    b_id = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    page_no = models.IntegerField()
    title = models.CharField(max_length = 200)
    text = models.TextField() 
    images = models.ManyToManyField(ImageModel, blank=True)

