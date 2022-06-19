from django.db import models

class phrase(models.Model):
    ru = models.CharField(max_length=80, verbose_name='Ru', help_text='Русский')
    en = models.CharField(max_length=80, verbose_name='En', help_text='English')

    def __str__(self):
        return self.ru

    class Meta:
        ordering = ['ru']
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
