# Generated by Django 2.1.4 on 2019-01-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_remove_postsell_commodity'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsell',
            name='pic',
            field=models.ImageField(default='', upload_to='commodity_pics'),
        ),
    ]
