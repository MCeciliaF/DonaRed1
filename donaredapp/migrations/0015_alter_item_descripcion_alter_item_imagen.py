# Generated by Django 5.2 on 2025-06-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaredapp', '0014_alter_item_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='imagen',
            field=models.ImageField(blank=True, default='items/sin_imagen.png', null=True, upload_to='items/'),
        ),
    ]
