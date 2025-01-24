from django import forms
from django.contrib import admin
from .models import Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # form = CategoryAdminForm
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ['-created_at']
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('slug',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category__name')
    ordering = ['-created_at']
    list_filter = ('category', 'created_at', 'updated_at')
    # raw_id_fields = ('category',)  
    readonly_fields = ('slug',)

    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.short_description = 'Category Name'
