from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from images.models import Image
import re
from .utils import embed_image

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=280)
    slug = models.SlugField(max_length=280, editable=False)
    section = models.CharField(choices=(
        ('nf', 'Nonfiction'),
        ('f', 'Fiction'),
        ('p', 'Poetry'),
    ))
    keywords = models.CharField(max_length=280)
    snippet = models.TextField()

    author = models.CharField(max_length=280)
    author_url = models.URLField(blank=True)
    author_email = models.EmailField(blank=True)

    cover_image = models.ForeignKey(Image, on_delete=models.RESTRICT, blank=True, null=True)

    content = models.TextField()
    content_images = models.ManyToManyField(Image, related_name='articles', blank=True)

    publication_date = models.DateField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[self.publication_date.year, self.publication_date.month, self.publication_date.day, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publication_date']

    @property
    def rendered_content(self):
        content = self.content
        rendered_content = re.sub('{{\s*image_(.*)\s*}}', lambda match :embed_image(match, self), content)
        return rendered_content