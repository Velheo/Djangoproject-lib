# Generated by Django 3.2.6 on 2021-08-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='year',
            field=models.ImageField(upload_to='', verbose_name=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
