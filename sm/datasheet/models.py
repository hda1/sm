from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=26, verbose_name='Наименование')
    leads = models.IntegerField(verbose_name='Количество выводов')
    aliases = models.CharField(blank=True, max_length=40, verbose_name='Псевдонимы')
    image = models.ImageField(blank=True, upload_to='img/packages/small')
    image_small_width = models.IntegerField(blank=True)
    image_small_height = models.IntegerField(blank=True)
    image_big = models.ImageField(blank=True, upload_to='img/packages/big')
    image_big_width = models.IntegerField(blank=True)
    image_big_height = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'



"""
class PartNumber(models.Model):
    code = models.CharField(max_length=20, verbose_name='Код маркировки')
    title = models.CharField(max_length=21, verbose_name='Короткое наименование')
    part_number = models.CharField(max_length=21, verbose_name='Полное наименование')
    package = models.ForeignKey(Package, verbose_name='Корпус')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')


    def __str__(self):
        return self.code + ' ---- ' + self.part_number

    class Meta:
        ordering = ['code']
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'
"""

