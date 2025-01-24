from django.db import models
from shared.models import TimeStampedUUID
from django.utils.translation import gettext_lazy as _ 
from autoslug import AutoSlugField


class Brand(TimeStampedUUID):
    name = models.CharField(verbose_name=_("Name of Brand"),max_length=255,unique=True)
    description = models.TextField(verbose_name=_("Description of Brand"),null=True,blank=True)
    brand_image = models.ImageField(verbose_name=_("Brand Image / Logo"),null=True,blank=True,upload_to="brand-images/",help_text=_("Upload an image for this brand."))
    slug = AutoSlugField(populate_from='name',unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ['-created_at']

    @property
    def get_brand_logo(self):
        try:
            url = self.brand_image.url
        except:
            url ='' 
        return url
