# Generated by Django 2.1.4 on 2019-02-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0048_auto_20190222_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='100', verbose_name='What is the least price you are selling your item for?'),
        ),
    ]
