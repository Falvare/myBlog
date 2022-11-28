from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    github = models.URLField(blank=True)
    url = models.URLField(blank=True)
    image1 = CloudinaryField(null=True, blank=True)
    image2 = CloudinaryField(null=True, blank=True)
    image3 = CloudinaryField(null=True, blank=True)
    technologies = models.TextField(blank=True)
    sectionLabel1 = models.CharField(max_length=250, blank=True)
    section1 = models.TextField()
    sectionLabel2 = models.CharField(max_length=250, blank=True)
    section2 = models.TextField(blank=True)
    sectionLabel3 = models.CharField(max_length=250, blank=True)
    section3 = models.TextField(blank=True)
    author = models.CharField(max_length=250, default="Francisco J. Alvidrez")
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title