from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from firm.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', ImportView.as_view(), name='import'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
