# Generated by Django 2.1.4 on 2019-02-22 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0047_auto_20190222_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid',
            new_name='bid_price',
        ),
    ]