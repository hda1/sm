#from django.shortcuts import render
from django.core import management
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class ImportView(TemplateView):

    def get(self, request, *args, **kwargs):
        #file_name = '/home/sam/Загрузки/Telegram Desktop/ChatExport_2022-05-15/result.json'
        #chat_name = import_json_chat(file_name)
        management.call_command('compilemessages', )
        return HttpResponse('Chat ' + 'chat_name')
