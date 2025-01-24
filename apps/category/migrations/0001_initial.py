# Generated by Django 5.1.5 on 2025-01-24 09:24

import autoslug.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name of Category')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of Category')),
                ('category_image', models.ImageField(blank=True, help_text='Upload an image for this category. Leave blank if not needed.', null=True, upload_to='categories/', verbose_name='Category Image')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of Sub-category')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of Subcategory')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='category.category')),
            ],
            options={
                'verbose_name': 'Sub-Category',
                'verbose_name_plural': 'sub-Categories',
                'ordering': ['-created_at'],
                'unique_together': {('name', 'category')},
            },
        ),
    ]
