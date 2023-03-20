from django.http import HttpResponse
from django.views.generic.base import TemplateView

from old_import.smd import *

class ImportView(TemplateView):

    def get(self, request, *args, **kwargs):
        #management.call_command('compilemessages', )
        return HttpResponse('<a href="/import/smd/">Import SMD</a>')


class ImportSmdView(TemplateView):

    def get(self, request, *args, **kwargs):
        import_smd()
        return HttpResponse('<a href="/import/"> Import </a><br>Import smd done!')




