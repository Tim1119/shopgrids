# Generated by Django 5.1.5 on 2025-01-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_discount_amount_product_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_digital',
            field=models.BooleanField(default=False, help_text='Tick if this product needs shipping or not.', verbose_name='Is Digital'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_trending',
            field=models.BooleanField(default=False, help_text='Tick if this product is a trending product.', verbose_name='Is Tredning'),
        ),
    ]
