#from django.conf import settings
#from django.conf.urls.static import static
#from django.contrib import admin
from django.urls import path

from old_import.views import *

urlpatterns = [


    path('smd/', ImportSmdView.as_view(), name='smd'),
    path('import/', ImportView.as_view(), name='import'),
    path('', ImportView.as_view()),
]
