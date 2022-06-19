# Generated by Django 3.2 on 2022-06-19 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru', models.CharField(help_text='Русский', max_length=80, verbose_name='Ru')),
                ('en', models.CharField(help_text='English', max_length=80, verbose_name='En')),
            ],
            options={
                'verbose_name': 'Перевод',
                'verbose_name_plural': 'Переводы',
                'ordering': ['ru'],
            },
        ),
    ]
