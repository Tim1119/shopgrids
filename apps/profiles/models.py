from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from shared.models import TimeStampedUUID

User = get_user_model()

class Profile(TimeStampedUUID):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User Profile"))
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, verbose_name=_("Avatar"))
    bio = models.TextField(max_length=500, null=True, blank=True, verbose_name=_("Bio"))
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("Phone Number"))
    address = models.TextField(null=True, blank=True, verbose_name=_("Address"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Date of Birth"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return f"Profile of {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering= ['-created_at']
