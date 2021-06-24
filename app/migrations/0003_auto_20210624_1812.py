# Generated by Django 2.2 on 2021-06-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210624_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='priority',
            field=models.IntegerField(choices=[(1, '低'), (2, '普通'), (3, '高')], default=2, verbose_name='優先度'),
        ),
    ]
