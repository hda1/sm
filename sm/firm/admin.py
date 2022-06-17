from django.contrib import admin

from .models import *


class FirmAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name', 'path', 'logo')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Firm, FirmAdmin)
admin.site.register(Tag, TagAdmin)
