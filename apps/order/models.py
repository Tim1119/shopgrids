from django.db import models
from shared.models import TimeStampedUUID
from .enums import OrderStatus
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.products.models import Product
from autoslug import AutoSlugField
from django_extensions.db.fields import RandomCharField
from apps.profiles.models import Profile
# Create your models here.

User = get_user_model()


class Order(TimeStampedUUID):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,verbose_name=_("User Profile"))
    order_status = models.CharField(max_length=12, choices=OrderStatus.choices, default=OrderStatus.PENDING,verbose_name=_("Order Status"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name=_("Total Price"))
    payment_method = models.CharField(max_length=50, verbose_name=_("Payment Method"), null=True, blank=True)
    is_paid = models.BooleanField(default=False,verbose_name="Is paid")
    slug = AutoSlugField(populate_from='user',unique=True)
    tracking_number = RandomCharField(length=12,unique=True,uppercase=True,lowercase=False,include_alpha=False,include_digits=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = f"TRK-{self.tracking_number_base}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering= ['-created_at']

    def get_total_quantity(self):
        return sum(item.quantity for item in self.order_items.all())
    
    @property
    def get_total_price(self):
        return sum(item.subtotal for item in self.order_items.all())

    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price
        super().save(*args, **kwargs)


class OrderItem(TimeStampedUUID):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Product Quantity"))
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Unit Price"))
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Subtotal"), editable=False)
    slug = AutoSlugField(populate_from='',unique=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order Item :{self.quantity} × {self.product.name} in Order #{self.order.id}"

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ['-created_at']

