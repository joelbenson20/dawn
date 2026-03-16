import re
from django.db import models
from django.urls import reverse
from dawn.utils import render

class Image(models.Model):

    image = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=280, unique=True)
    
    title = models.CharField(max_length=280, default="Untitled")
    caption = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=280)

    author = models.CharField(max_length=280, blank=True, null=True)
    author_url = models.URLField(blank=True, null=True)

    upload_date = models.DateTimeField(auto_now_add=True, editable=False)
    publication_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('image', args=[self.publication_date.year, self.publication_date.month, self.publication_date.day, self.slug])

    class Meta:
        ordering = ['-upload_date', '-slug']

    @property
    def get_model(self):
        return self.__class__.__name__
    
    @property
    def rendered_caption(self):
        return render(self.caption)