from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "date_of_birth", "created_at")
    search_fields = ("user__first_name","user__last_name", "user__email", "phone_number")
