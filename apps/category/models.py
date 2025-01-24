from django.db import models
from shared.models import TimeStampedUUID
from django.utils.translation import gettext_lazy as _ 
from autoslug import AutoSlugField
# Create your models here.
class Category(TimeStampedUUID):
    name = models.CharField(verbose_name=_("Name of Category"),max_length=255,unique=True)
    description = models.TextField(verbose_name=_("Description of Category"),null=True,blank=True)
    category_image = models.ImageField(verbose_name=_("Category Image"),upload_to="categories-images/",null=True,blank=True,help_text=_("Upload an image for this category. Leave blank if not needed."))
    slug = AutoSlugField(populate_from='name',unique=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['-created_at']


class Subcategory(TimeStampedUUID):
    name = models.CharField(verbose_name=_("Name of Sub-category"),max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("Description of Subcategory"),null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategories")
    slug = AutoSlugField(populate_from='name',unique=True)

    def __str__(self):
        return f"{self.name} Sub cetgory for {self.category.name} Category"
    
    class Meta:
        verbose_name = _("Sub-Category")
        verbose_name_plural = _("sub-Categories")
        ordering = ['-created_at']
        unique_together = ('name', 'category')