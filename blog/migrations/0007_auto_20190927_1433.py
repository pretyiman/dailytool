# Generated by Django 2.2.2 on 2019-09-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190925_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Sale_Price',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Stock',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
