from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=75, verbose_name='Расположение')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'
