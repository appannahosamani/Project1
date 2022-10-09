# Generated by Django 4.0.6 on 2022-08-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0006_remove_products_database_id_products_database_medium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('Product_Price', models.IntegerField()),
                ('Product_Image', models.ImageField(upload_to='images/%y')),
                ('Product_Description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Products_Database',
        ),
    ]