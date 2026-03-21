from django.contrib import admin
from .models import Image, Fragment


class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'slug', 'description'
    )

    fieldsets = (
        (None, {
            'fields': ('slug', 'image', 'description')
        }),
    )

class FragmentAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'content',
        'modified_datetime',
    )

    fieldsets = (
        (None, {
            'fields': ('id', 'content', 'fragments', 'images')
        }),
    )

    filter_horizontal = ('fragments', 'images')

admin.site.register(Fragment, FragmentAdmin)
admin.site.register(Image, ImageAdmin)
