# Generated by Django 4.0.6 on 2022-07-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('Basic_sal', models.IntegerField()),
                ('No_of_OT', models.IntegerField()),
            ],
        ),
    ]