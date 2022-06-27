from django.contrib import admin

from .models import *

class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Position, PositionAdmin)
