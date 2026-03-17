from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from hyper.utils import hyperrender


# Create your models here.

class Image(models.Model):

    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
    
    class Meta:
        ordering = ['-modified_datetime']

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
    cover_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    content_images = models.ManyToManyField(Image, related_name='dawn_articles', blank=True)

    @property
    def rendered_content(self):
        return hyperrender(self.content, self)

class DawnImage(DawnObject):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)