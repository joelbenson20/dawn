from django.db import models
from .render import hyperrender_content

class Image(models.Model):

    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + self.slug
    
    class Meta:
        ordering = ['-modified_datetime']

class Fragment(models.Model):

    content = models.TextField()
    fragments = models.ManyToManyField('self', symmetrical=False, related_name='parent_fragments', blank=True)
    images = models.ManyToManyField(Image, related_name='fragments', blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + self.content[:50] + '...'

    @property
    def rendered_content(self):
        return hyperrender_content(self)
    
    class Meta:
        ordering = ['-modified_datetime']
