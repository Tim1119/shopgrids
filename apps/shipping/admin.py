from django.contrib import admin

# Register your models here.
from django.contrib import admin
from apps.shipping.models import Shipping


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'address_line_1',
        'city',
        'state',
        'country',
        'delivery_method',
        'tracking_number',
        'shipped_date',
        'estimated_delivery_date',
    )
    list_filter = ('state', 'country', 'delivery_method', 'shipped_date')
    search_fields = (
        'order__id',
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'zip_code',
        'tracking_number',
    )
    ordering = ('-shipped_date',)
    readonly_fields = ('order', 'shipped_date', 'tracking_number', 'estimated_delivery_date')
