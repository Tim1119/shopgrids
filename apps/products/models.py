from django.db import models
from shared.models import TimeStampedUUID
from django.utils.translation import gettext_lazy as _ 
from autoslug import AutoSlugField
from apps.category.models import Category,Subcategory
from .enums import ProductColors,ProductImageTypes
from apps.brands.models import Brand
from django.core.exceptions import ValidationError
# Create your models here.

class Product(TimeStampedUUID):

    name = models.CharField(max_length=255,verbose_name=_("Product name"),unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Product Price"))
    product_description = models.TextField(verbose_name=_("Product Description"),null=True,blank=True)
    product_image = models.ImageField(verbose_name=_("Product Image"),upload_to="products-images/",null=True,blank=True,help_text=_("Upload an image for this product."))
    product_color = models.CharField(verbose_name=_("Product Color"),max_length=100,choices=ProductColors.choices,default=ProductColors.BLACK)
    size = models.CharField(verbose_name=_("Product Size"), max_length=50, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(verbose_name=_("Stock Quantity"), help_text=_("The number of units available in stock."), default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    sub_category = models.ForeignKey(Subcategory, verbose_name=_("Sub-Category"),on_delete=models.CASCADE)
    product_weight = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Product Weight"),blank=True,null=True)
    product_dimension = models.CharField(max_length=255,verbose_name=_("Product Dimension"),blank=True,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Brand"))
    is_digital = models.BooleanField(verbose_name=_("Is Product digital"), default=True, help_text=_("Tick if this product needs shipping or not."))
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True, help_text=_("Tick to make the product available for sale."))
    slug = AutoSlugField(populate_from='name',unique=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def clean(self):
        # Perform the category validation in the clean method to ensure the subcategory belongs to the product's category
        if self.sub_category.category.name != self.category.name:
            raise ValidationError(_("The selected subcategory does not belong to the same category as the product."))

        super().clean()  # Don't forget to call the parent method to ensure any other validation is executed.





class ProductImage(TimeStampedUUID):
    product = models.ForeignKey('Product', related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-images/', verbose_name=_("Product Image"))
    image_type = models.CharField(max_length=10,choices=ProductImageTypes.choices,default=ProductImageTypes.MAIN,verbose_name=_("Image Type"))
    alt_text = models.CharField(max_length=255, verbose_name=_("Alt Text"), null=True, blank=True)
    slug = AutoSlugField(populate_from='image',unique=True)

    def __str__(self):
        return f"{self.image_type} for {self.product.name}"

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        constraints = [
            models.UniqueConstraint(fields=['product', 'image_type'], condition=models.Q(image_type=ProductImageTypes.MAIN), name='unique_main_image')
        ]
