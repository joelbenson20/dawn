from django.contrib import admin
from .models import DawnArticle, DawnImage, Image

class DawnArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author_name',
        'publication_date',
    )

    list_filter = (
        'published',
        'type',
    )

    fieldsets = (
        (None, {
            'fields': ('type', 'title', 'description', 'keywords',),
        }),
        ('Author Information', {
            'fields': ('author_name', 'author_url'),
        }),
        ('Content', {
            'fields': ('content', 'cover_image', 'content_images'),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published',),
        })
    )

    filter_horizontal = ('content_images',)

class DawnImageAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author_name',
        'publication_date',
    )

    list_filter = (
        'published',
        'type',
    )

    fieldsets = (
        (None, {
            'fields': ('type', 'title', 'description', 'keywords',),
        }),
        ('Author Information', {
            'fields': ('author_name', 'author_url'),
        }),
        ('Content', {
            'fields': ('image',),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published',),
        })
    )

class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'slug', 'description'
    )

    fieldsets = (
        (None, {
            'fields': ('slug', 'image', 'description')
        }),
    )



admin.site.register(DawnArticle, DawnArticleAdmin)
admin.site.register(DawnImage, DawnImageAdmin)
admin.site.register(Image, ImageAdmin)