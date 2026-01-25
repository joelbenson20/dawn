from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'slug',
        'caption',
        'author',
        'author_email',
        'upload_date'
    )

    list_filter = (
        'published',
    )

    fieldsets = (
        (None, {
            'fields': ('image', 'caption', 'slug', 'keywords',),
        }),
        ('Author Information', {
            'fields': ('author', 'author_email', 'author_url'),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published',),
        })
    )

admin.site.register(Image, ImageAdmin)