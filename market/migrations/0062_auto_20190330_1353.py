# Generated by Django 2.1.7 on 2019-03-30 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0061_auto_20190318_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='live_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sell_on',
        ),
    ]
