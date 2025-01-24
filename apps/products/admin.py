from django.contrib import admin
from .models import Product
from apps.category.models import Category, Subcategory
from apps.brands.models import Brand
from django.utils.translation import gettext_lazy as _

# Customizing the ProductAdmin to manage products and associated fields in the admin interface
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'category', 'sub_category', 'stock_quantity', 'is_active', 'is_trending','is_special_offer', 'is_digital', 'brand', 'created_at'
    )
    list_filter = ('category', 'sub_category', 'brand', 'is_active', 'is_trending')
    search_fields = ('name', 'category__name', 'sub_category__name', 'brand__name')

    
    # Fields to show in the form and their grouping
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'product_image','product_description', 'category', 'sub_category', 'brand', 'product_color', 'size', 'product_weight', 'product_dimension',  'is_digital', 'is_trending','is_special_offer', 'is_active', 'discount_percentage', 'discount_amount')
        }),
        (_("Images"), {
            'fields': ('product_image_alt_1', 'product_image_alt_2', 'product_image_alt_3', 'product_image_alt_4')
        }),
    )
    
    # Display the discounted price in the admin interface
    def get_discounted_price(self, obj):
        return obj.get_discounted_price()
    get_discounted_price.short_description = _("Discounted Price")

    # Customizing the save behavior if needed
    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Product, ProductAdmin)
