# Generated by Django 4.0.6 on 2022-08-09 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products_details',
            name='Product_Image',
        ),
        migrations.RemoveField(
            model_name='products_details',
            name='product_Size',
        ),
    ]
