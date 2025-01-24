from django.db import models
from apps.order.models import Order
from shared.models import TimeStampedUUID
# Create your models here.
class Shipping(TimeStampedUUID):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="shipping", verbose_name=_("Order"))
    address_line_1 = models.CharField(max_length=255, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    state = models.CharField(max_length=100, verbose_name=_("State"))
    zip_code = models.CharField(max_length=20, verbose_name=_("Zip Code"))
    country = models.CharField(max_length=100, verbose_name=_("Country"))
    delivery_method = models.CharField(max_length=50, verbose_name=_("Delivery Method"), default="Standard")
    tracking_number = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Tracking Number"))
    shipped_date = models.DateTimeField(null=True, blank=True, verbose_name=_("Shipped Date"))
    estimated_delivery_date = models.DateTimeField(null=True, blank=True, verbose_name=_("Estimated Delivery Date"))

    def __str__(self):
        return f"Shipping for Order #{self.order.id}"

    class Meta:
        verbose_name = _("Shipping")
        verbose_name_plural = _("Shipping")
