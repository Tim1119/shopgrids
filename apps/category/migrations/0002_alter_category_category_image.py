# Generated by Django 5.1.5 on 2025-01-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, help_text='Upload an image for this category. Leave blank if not needed.', null=True, upload_to='categories-images/', verbose_name='Category Image'),
        ),
    ]
