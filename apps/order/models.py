from django.db import models
from shared.models import TimeStampedUUID
from .enums import OrderStatus
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.products.models import Product
from autoslug import AutoSlugField
# Create your models here.

User = get_user_model()


class Order(TimeStampedUUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name=_("User"))
    order_status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING,verbose_name=_("Order Status"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name=_("Total Price"))
    payment_method = models.CharField(max_length=50, verbose_name=_("Payment Method"), null=True, blank=True)
    is_paid = models.BooleanField(default=False,verbose_name="Has order been paid for?")
    slug = AutoSlugField(populate_from='user',unique=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering= ['-created_at']


class OrderItem(TimeStampedUUID):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Product Quantity"))
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Unit Price"))
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Subtotal"), editable=False)
    slug = AutoSlugField(populate_from='order',unique=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order Item :{self.quantity} × {self.product.name} in Order #{self.order.id}"

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ['-created_at']

