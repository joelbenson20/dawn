from django.contrib import admin
from .models import DawnArticle, DawnImage

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
            'fields': ('content',),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published',),
        })
    )

admin.site.register(DawnArticle, DawnArticleAdmin)

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

admin.site.register(DawnImage, DawnImageAdmin)