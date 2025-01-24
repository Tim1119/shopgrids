from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'image_preview', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ['-created_at']
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('slug',)

    def image_preview(self, obj):
        """
        Display a small preview of the brand image/logo in the admin list view.
        """
        if obj.brand_image:
            return mark_safe(f'<img src="{obj.brand_image.url}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />')
        return "No Image"
    image_preview.short_description = "Image Preview"
