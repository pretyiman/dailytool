# Generated by Django 2.2.2 on 2019-09-25 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190925_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Warehousse',
            new_name='Warehouse',
        ),
    ]
