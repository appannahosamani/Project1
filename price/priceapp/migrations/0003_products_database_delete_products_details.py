# Generated by Django 4.0.6 on 2022-08-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0002_remove_products_details_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products_Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('Product_Price', models.IntegerField()),
                ('Product_Image', models.ImageField(upload_to='media/')),
                ('product_Size', models.BooleanField()),
                ('Product_Description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Products_Details',
        ),
    ]
