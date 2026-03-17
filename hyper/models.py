from django.db import models

class Image(models.Model):

    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
    
    class Meta:
        ordering = ['-modified_datetime']

class Fragment(models.Model):

    slug = models.SlugField(unique=True)
    content = models.TextField()
    fragments = models.ManyToManyField('self', symmetrical=False, related_name='parent_fragments', blank=True)
    images = models.ManyToManyField(Image, related_name='fragments', blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug + ":" + self.content[:50]
    
    class Meta:
        ordering = ['-modified_datetime']
