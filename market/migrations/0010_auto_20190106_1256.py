# Generated by Django 2.1.4 on 2019-01-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20190104_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsell',
            name='commodity',
            field=models.ImageField(default='', null=True, upload_to='commodity_pics'),
        ),
    ]