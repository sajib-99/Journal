from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=9999)
    author=models.CharField(max_length=9999)
    slug=models.CharField(max_length=1000)
    timeStamp=models.DateTimeField(blank=True)
    content= RichTextField(blank=True, null=True)
    manuscript = models.FileField(upload_to='manuscripts/')
    #content=models.TextField()

    # class Meta:
    #     ordering = ['-sno',]

    def __str__(self):
        return self.title + " - by - " + self.author