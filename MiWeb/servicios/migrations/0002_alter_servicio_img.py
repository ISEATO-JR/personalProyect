# Generated by Django 4.2.7 on 2024-03-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='img',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]