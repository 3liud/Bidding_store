# Generated by Django 2.1.4 on 2019-03-17 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0052_auto_20190317_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sell_on_date',
            new_name='sell_on',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sell_on_time',
        ),
    ]
