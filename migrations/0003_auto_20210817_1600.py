# Generated by Django 2.1 on 2021-08-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=25),
        ),
    ]
