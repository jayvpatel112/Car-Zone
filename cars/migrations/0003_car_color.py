# Generated by Django 4.0.4 on 2022-06-03 16:23

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_description_alter_car_doors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
    ]
