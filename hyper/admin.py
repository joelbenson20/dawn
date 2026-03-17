from django.contrib import admin

from .models import Fragment

class FragmentAdmin(admin.ModelAdmin):
    
    list_display = (
        'slug',
        'content',
    )

admin.site.register(Fragment, FragmentAdmin)

