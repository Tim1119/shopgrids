from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_status', 'total_price', 'is_paid', 'created_at', 'updated_at')
    list_filter = ('order_status', 'is_paid', 'created_at', 'updated_at')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'id')
    ordering = ('-created_at',)
    readonly_fields = ('slug', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'order_status', 'total_price', 'payment_method', 'is_paid', 'slug')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


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
