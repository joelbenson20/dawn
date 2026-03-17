from django.db import models

class Fragment(models.Model):

    slug = models.SlugField(unique=True)
    content = models.TextField()
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug + ":" + self.content[:50]
    
    class Meta:
        ordering = ['-modified_datetime']
