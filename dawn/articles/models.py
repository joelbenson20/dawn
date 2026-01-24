from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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

    cover_image = models.ImageField(upload_to='images/', blank=True)
    cover_image_credit = models.TextField(blank=True)

    content = models.TextField()

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