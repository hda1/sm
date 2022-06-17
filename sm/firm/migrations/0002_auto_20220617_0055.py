# Generated by Django 3.2 on 2022-06-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(help_text='Разделы в которых отображается эта фирма', max_length=40, verbose_name='Тег'),
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Фирма')),
                ('full_name', models.CharField(default='', max_length=100, verbose_name='Полное наименование')),
                ('path', models.CharField(blank=True, max_length=40, verbose_name='Вебсайт')),
                ('img', models.ImageField(blank=True, upload_to='img/firm')),
                ('img_width', models.IntegerField(default=0, editable=False)),
                ('img_height', models.IntegerField(default=0, editable=False)),
                ('tag', models.ManyToManyField(blank=True, to='firm.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Фирму',
                'verbose_name_plural': 'Фирмы',
                'ordering': ['title'],
            },
        ),
    ]
