from django.contrib import admin

from .models import *


class PhraseAdmin(admin.ModelAdmin):
    list_display = ('ru', 'en')

admin.site.register(Phrase, PhraseAdmin)