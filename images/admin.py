from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'slug',
        'caption',
        'author',
        'upload_date'
    )

    list_filter = (
        'published',
    )

    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'caption', 'slug', 'keywords',),
        }),
        ('Author Information', {
            'fields': ('author', 'author_url'),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published',),
        })
    )

admin.site.register(Image, ImageAdmin)