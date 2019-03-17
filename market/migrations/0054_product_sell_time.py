# Generated by Django 2.1.4 on 2019-03-17 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0053_auto_20190317_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sell_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Set the time for the Auction'),
        ),
    ]
