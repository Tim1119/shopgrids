from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Product, ProductImage
from apps.category.models import Category, Subcategory
from apps.brands.models import Brand
from django.db import models
from django.core.exceptions import ValidationError
from .enums import ProductImageTypes

admin.site.register(Product)
admin.site.register(ProductImage)

# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 5  # Allows up to 5 empty fields for new images by default
#     fields = ('image', 'image_type', 'alt_text')
#     readonly_fields = ('image',)  # Make the image field readonly since it's an upload field

#     def has_add_permission(self, request, obj=None):
#         # Allow only one main image to be added
#         if obj and ProductImage.objects.filter(product=obj, image_type=ProductImageTypes.MAIN).exists():
#             self.extra = 0  # Hide extra image fields if a main image already exists
#         return super().has_add_permission(request, obj)

#     def has_delete_permission(self, request, obj=None):
#         # Allow deleting images except for the main image
#         if obj and ProductImage.objects.filter(product=obj, image_type=ProductImageTypes.MAIN).count() == 1:
#             return False  # Prevent deletion of the main image
#         return super().has_delete_permission(request, obj)

# class ProductAdminForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Dynamically adjust fields visibility based on the category field visibility settings
#         if self.instance.category:
#             # You can add custom logic for hiding fields based on category here
#             pass

#         # Lazy load the 'brand' model if needed
#         self.fields['brand'].queryset = Brand.objects.all()

#     def clean(self):
#         # Perform the category validation in the clean method to ensure the subcategory belongs to the product's category
#         if self.instance.sub_category:
#             for subcat in self.instance.sub_category.all():
#                 if self.instance.category != subcat.category:
#                     raise ValidationError(_("The selected subcategory does not belong to the same category as the product."))
#         super().clean()

# # Register Product Model
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     form = ProductAdminForm  # Use the custom form for conditional fields
#     list_display = ('name', 'price', 'category', 'stock_quantity', 'is_active', 'slug')
#     list_filter = ('category', 'sub_category', 'brand', 'is_active')
#     search_fields = ('name', 'product_description')
#     prepopulated_fields = {'slug': ('name',)}
#     ordering = ['-created_at']
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'price', 'product_description', 'product_image', 'product_color', 'size', 'stock_quantity', 'category', 'sub_category', 'brand', 'is_active')
#         }),
#     )
#     inlines = [ProductImageInline]

# # Register ProductImage Model
# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('product', 'image_type', 'alt_text')
#     list_filter = ('image_type',)
#     search_fields = ('alt_text',)
#     ordering = ['product', '-created_at']

#     def get_readonly_fields(self, request, obj=None):
#         # Make image type read-only for gallery images in the admin form
#         if obj and obj.image_type == ProductImageTypes.MAIN:
#             return ('image_type',)  # Make the image type read-only for the main image
#         return super().get_readonly_fields(request, obj)

#     def get_inline_instances(self, request, obj=None):
#         # Allow the inline form for ProductImage only if the product has images
#         if obj and obj.product_images.exists():
#             return super().get_inline_instances(request, obj)
#         return []
