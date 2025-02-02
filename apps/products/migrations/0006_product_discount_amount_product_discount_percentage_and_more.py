# Generated by Django 5.1.5 on 2025-01-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_is_shipping_required_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discount Amount'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Discount Percentage'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_trending',
            field=models.BooleanField(default=True, help_text='Tick if this product is a trending product.', verbose_name='Is Tredning'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_digital',
            field=models.BooleanField(default=True, help_text='Tick if this product needs shipping or not.', verbose_name='Is Digital'),
        ),
    ]
