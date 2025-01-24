from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Subcategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}  
    ordering = ['-created_at']
    list_filter = ('created_at', 'updated_at')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category__name')
    prepopulated_fields = {'slug': ('name',)}  
    ordering = ['-created_at']
    list_filter = ('category', 'created_at', 'updated_at')
    raw_id_fields = ('category',)  

    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.short_description = 'Category Name'
