#from django.shortcuts import render
from django.core import management
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class ImportView(TemplateView):

    def get(self, request, *args, **kwargs):
        management.call_command('compilemessages', )
        return HttpResponse('Chat ' + 'chat_name')
