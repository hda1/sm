from django.contrib import admin

from .models import *

class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'leads', 'aliases')
    list_filter = ('leads',)


admin.site.register(Package, PackageAdmin)
