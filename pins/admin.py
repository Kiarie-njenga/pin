







from django.contrib import admin

from .models import Pin, Comment

class PinAdmin(admin.ModelAdmin):
    list_display=['title', 'user', 'phone']
    search_fields=['phone']
    list_filter=['date_created']
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Pin, PinAdmin)
admin.site.register(Comment)
