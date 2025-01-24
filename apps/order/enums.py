from django.db import models
from django.utils.translation import gettext_lazy as _ 

class OrderStatus(models.TextChoices):
        PENDING = 'P', _("Pending")
        PAID = 'PA', _("Paid")
        SHIPPED = 'S', _("Shipped")
        DELIVERED = 'D', _("Delivered")
        CANCELLED = 'C', _("Cancelled")
