# Generated by Django 2.1.4 on 2019-01-07 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_postsell_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsell',
            name='pic',
        ),
    ]
