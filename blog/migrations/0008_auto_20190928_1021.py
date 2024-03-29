# Generated by Django 2.2.2 on 2019-09-28 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190927_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.catagory'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Rack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.rack'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Sub_Catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.subcatagory'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.warehouse'),
        ),
    ]
