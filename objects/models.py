from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from dawn.utils import hyperrender


# Create your models here.
class DawnObject(models.Model):

    type = models.CharField(choices=(
        ('nf', 'Nonfiction'),
        ('f', 'Fiction'),
        ('p', 'Poetry'),
        ('i', 'Image'),
    ))

    title = models.CharField(max_length=280)
    slug = models.SlugField(max_length=280, editable=False)
    description = models.TextField(blank=True)
    keywords = models.CharField(max_length=280)

    author_name = models.CharField(max_length=280)
    author_url = models.URLField(blank=True)

    publication_date = models.DateField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('object', args=[self.get_model.lower(), self.publication_date.year, self.publication_date.month, self.publication_date.day, self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(DawnObject, self).save(*args, **kwargs)
    
    class Meta:
        abstract = True
        ordering = ['-publication_date']

    @property
    def get_model(self):
        return self.__class__.__name__

class DawnArticle(DawnObject):

    content = models.TextField()

    @property
    def rendered_content(self):
        return hyperrender(self.content, self)

class DawnImage(DawnObject):

    image = models.ImageField(upload_to='objects/images/')