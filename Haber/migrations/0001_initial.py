# Generated by Django 3.0 on 2019-12-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Haberin Adı')),
                ('content', models.TextField(verbose_name='Haberin İçeriği')),
                ('date', models.DateTimeField(max_length=50, verbose_name='Tarih')),
                ('editor', models.CharField(max_length=50, verbose_name='Haberi Yayınlayan')),
            ],
            options={
                'verbose_name': 'Haber',
                'verbose_name_plural': 'Haber',
            },
        ),
    ]
