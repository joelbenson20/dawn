from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'author_email',
        'publication_date',
    )

    list_filter = (
        'published',
    )

    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
        ('Author Information', {
            'fields': ('author', 'author_email', 'author_url'),
        }),
        ('Cover Image', {
            'fields': ('cover_image', 'cover_image_credit'),
        }),
        ('Content', {
            'fields': ('content', 'keywords'),
        }),
        ('Publication', {
            'fields': ('publication_date', 'published'),
        })
    )

admin.site.register(Article, ArticleAdmin)
