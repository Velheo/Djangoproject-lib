# Generated by Django 3.2.6 on 2021-08-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_alter_author_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
