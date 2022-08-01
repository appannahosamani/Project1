# Generated by Django 4.0.6 on 2022-07-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmodel',
            name='Calories',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='Expiry_Date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='Packet_Id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='Packet_Type',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='Packet_content',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='Quantity_in_Litres',
            field=models.IntegerField(blank=True),
        ),
    ]
