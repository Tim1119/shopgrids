from django.db import models
from django.utils.translation import gettext_lazy as _ 

class ProductImageTypes(models.TextChoices):
        MAIN = 'main', _("Main Image")
        GALLERY = 'gallery', _("Gallery Image")
        ZOOM = 'zoom', _("Zoom Image")

class ProductColors(models.TextChoices):
    RED = "Red", _("Red")
    BLUE = "Blue", _("Blue")
    GREEN = "Green", _("Green")
    YELLOW = "Yellow", _("Yellow")
    BLACK = "Black", _("Black")
    WHITE = "White", _("White")
    OTHER = "Other", _("Other")