from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, editable=False)

    author = models.CharField(max_length=200)
    author_url = models.URLField(blank=True)
    author_email = models.EmailField(blank=True)

    cover_image = models.ImageField(upload_to='images/')
    cover_image_credit = models.CharField(max_length=200)

    content = models.TextField()

    publication_date = models.DateField()
    published = models.BooleanField(default=False)
    keywords = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[self.publication_date.year, self.publication_date.month, self.publication_date.day, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publication_date']