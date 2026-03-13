from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'publication_date',
    )

    list_filter = (
        'published',
        'section',
    )

    fieldsets = (
        (None, {
            'fields': ('title', 'snippet', 'section', 'keywords',),
        }),
        ('Author Information', {
            'fields': ('author', 'author_url'),
        }),
        ('Cover Image', {
            'fields': ('cover_image',),
        }),
        ('Content', {
            'fields': ('content', 'content_images',),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published',),
        })
    )

    filter_horizontal = ('content_images',)

admin.site.register(Article, ArticleAdmin)
