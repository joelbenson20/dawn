from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from hyper.render import hyperrender_content
from hyper.models import Image, Fragment
# from bs4 import BeautifulSoup

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
    fragments = models.ManyToManyField(Fragment, related_name='dawn_articles', blank=True)
    images = models.ManyToManyField(Image, related_name='dawn_articles', blank=True)
    cover_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)

    # def save(self, *args, **kwargs):
        
    #     self.createAndEmbedHyperframes()
    #     super().save(*args, **kwargs)
    
    # def createAndEmbedHyperframes(self, *args, **kwargs):

    #     soup = BeautifulSoup(self.content, 'html.parser')
    #     hyper_frames_sorted = sorted(soup.find_all('hyper-frame'), key=lambda x: len(x.find_parents('hyper-frame')), reverse=True)
        
    #     for hyper_frame in hyper_frames_sorted:

    #         #Only create Fragment if one has not already been created
    #         if (not hyper_frame.has_attr('id')):

    #             text = hyper_frame['text']
    #             rendered_hyper_frame = soup.new_tag('span', string=text)
    #             hyper_frame.replace_with(rendered_hyper_frame)
                
    #             Fragment.objects.create(content=text)
                
    #             rendered_hyper_frame['id'] = "new-id"
                        
    #     print(soup)
    #     return
    
    @property
    def rendered_content(self):
        return hyperrender_content(self)

class DawnImage(DawnObject):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)