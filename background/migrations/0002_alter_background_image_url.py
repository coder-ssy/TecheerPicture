# Generated by Django 5.0.6 on 2024-07-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
