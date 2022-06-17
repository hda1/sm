from PIL import Image
from sorl.thumbnail import get_thumbnail

from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe


class Tag(models.Model):
    title = models.CharField(max_length=40, verbose_name='Тег', help_text='Разделы в которых отображается эта фирма')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Firm(models.Model):
    title = models.CharField(max_length=35, verbose_name='Фирма')
    full_name = models.CharField(max_length=100, default='', verbose_name='Полное наименование')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    path = models.CharField(max_length=40, blank=True, verbose_name='Вебсайт')
    img = models.ImageField(blank=True, upload_to='img/firm')
    img_width = models.IntegerField(default=0, editable=False)
    img_height = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Firm, self).save(*args, **kwargs)

        try:
            im = Image.open(self.img.path)
            self.img_width = im.size[0]
            self.img_height = im.size[1]
        except:
            pass

        super(Firm, self).save(*args, **kwargs)

    def logo(self):
        if self.img:
            return mark_safe('<img src="%s%s" width="80"/>' % (
                                                settings.MEDIA_URL,
                                                get_thumbnail(self.img, '100')))

        else:
            return ''

    logo.short_description = 'Логотип'

    class Meta:
        ordering = ['title']
        verbose_name = 'Фирму'
        verbose_name_plural = 'Фирмы'
