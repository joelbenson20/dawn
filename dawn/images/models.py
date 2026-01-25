from django.db import models
from django.urls import reverse

class Image(models.Model):

    image = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True)
    slug = models.CharField(max_length=280)
    keywords = models.CharField(max_length=280)

    author = models.CharField(max_length=280, blank=True)
    author_url = models.URLField(blank=True)
    author_email = models.EmailField(blank=True)

    upload_date = models.DateTimeField(auto_now_add=True, editable=False)
    publication_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        print(self.publication_date)
        print(self.publication_date.year)
        print(self.publication_date.month)
        print(self.publication_date.day)
        return reverse('image', args=[self.publication_date.year, self.publication_date.month, self.publication_date.day, self.slug])

    class Meta:
        ordering = ['-upload_date', '-slug']