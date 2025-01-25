from django.db import models
from shared.models import TimeStampedUUID
from django.utils.translation import gettext_lazy as _ 
from autoslug import AutoSlugField
from apps.category.models import Category,Subcategory
from .enums import ProductColors,ProductImageTypes
from apps.brands.models import Brand
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
from decimal import Decimal
# Create your models here.


# todo: add that special offer cannot also be trending
#add rich text editor for features
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
    is_special_offer = models.BooleanField(verbose_name=_("Is Special Offer"), default=False, help_text=_("Tick if this product is a special offer."))
    is_digital = models.BooleanField(verbose_name=_("Is Digital"), default=False, help_text=_("Tick if this product needs shipping or not."))
    is_trending = models.BooleanField(verbose_name=_("Is Trending"), default=False, help_text=_("Tick if this product is a trending product."))
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True, help_text=_("Tick to make the product available for sale."))
    discount_percentage = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], null=True, blank=True, verbose_name=_("Discount Percentage"))
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Discount Amount"))
    product_image_alt_1 = models.ImageField(verbose_name=_("Product Image Alt 1"),upload_to="products-images/",null=True,blank=True,help_text=_("Upload an image for this product."))
    product_image_alt_2 = models.ImageField(verbose_name=_("Product Image Alt 2"),upload_to="products-images/",null=True,blank=True,help_text=_("Upload an image for this product."))
    product_image_alt_3 = models.ImageField(verbose_name=_("Product Image Alt 3"),upload_to="products-images/",null=True,blank=True,help_text=_("Upload an image for this product."))
    product_image_alt_4 = models.ImageField(verbose_name=_("Product Image Alt 4"),upload_to="products-images/",null=True,blank=True,help_text=_("Upload an image for this product."))
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
        
        if self.discount_percentage and self.discount_amount:
            raise ValidationError(_("You can only provide one of discount percentage or discount amount, not both."))
        
        if self.is_special_offer and self.is_trending:
            raise ValidationError(_("A product can only be special offer or trending but not both"))


        super().clean()  # Don't forget to call the parent method to ensure any other validation is executed.

    @property
    def get_discounted_price(self):
        """Calculate and return the discounted price based on either percentage or amount."""
        if self.discount_percentage:
            discount_value = (Decimal(self.discount_percentage) / Decimal(100)) * self.price
            return self.price - discount_value
        elif self.discount_amount:
            return self.price - self.discount_amount
        return self.price
    
    def get_image_url(self, image_field):
        """
        Helper method to return the URL of an image field or empty string if not available.
        """
        try:
            if image_field:
                return image_field.url
        except:
            return ''  
        return ''

    @property
    def get_main_product_image(self):
        return self.get_image_url(self.product_image)

    @property
    def get_product_image_alt_1(self):
        return self.get_image_url(self.product_image_alt_1)

    @property
    def get_product_image_alt_2(self):
        return self.get_image_url(self.product_image_alt_2)

    @property
    def get_product_image_alt_3(self):
        return self.get_image_url(self.product_image_alt_3)

    @property
    def get_product_image_alt_4(self):
        return self.get_image_url(self.product_image_alt_4)

