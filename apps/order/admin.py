from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_status', 'total_price', 'is_paid', 'created_at', 'updated_at')
    list_filter = ('order_status', 'is_paid', 'created_at', 'updated_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__email', 'id')
    ordering = ('-created_at',)
    readonly_fields = ('slug', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('customer', 'order_status', 'total_price', 'payment_method', 'is_paid', 'slug')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    def delete_model(self, request, obj):
        try:
            super().delete_model(request, obj)
        except Exception as e:
            self.message_user(request, f"Error: {str(e)}", level='error')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'unit_price', 'subtotal', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('order__id', 'product__name', 'order__user__first_name', 'order__user__last_name')
    ordering = ('-created_at',)
    readonly_fields = ('slug', 'subtotal', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('order', 'product', 'quantity', 'unit_price', 'subtotal', 'slug')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
