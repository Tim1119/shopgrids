# Generated by Django 5.1.5 on 2025-01-24 12:35

import autoslug.fields
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=django_extensions.db.fields.RandomCharField(blank=True, editable=False, include_alpha=False, length=12, unique=True, uppercase=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Is paid'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('P', 'Pending'), ('PA', 'Paid'), ('S', 'Shipped'), ('D', 'Delivered'), ('C', 'Cancelled')], default='P', max_length=12, verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='', unique=True),
        ),
    ]
