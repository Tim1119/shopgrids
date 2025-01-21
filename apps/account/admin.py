from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from .models import User
from django.contrib.auth.admin import UserAdmin

# Get the custom user model (ensure it's the correct model)
User = get_user_model()


# Custom UserAdmin class
class CustomUserAdmin(UserAdmin):
    # Define the form for user creation and change
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'role', 'is_verified')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_active', 'is_verified', 'is_staff')}
        ),
    )

    list_display = ('email', 'first_name', 'last_name', 'role', 'is_verified', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff', 'is_verified')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)
    filter_horizontal = ('groups', 'user_permissions')

    # Actions for the admin panel
    actions = ['make_verified', 'make_inactive']
    
    def make_inactive(self, request, queryset):
        """Deactivate selected users"""
        updated_count = queryset.update(is_active=False)
        self.message_user(request, f'{updated_count} user(s) marked as inactive.')
    make_inactive.short_description = _('Mark selected users as inactive')


# Register the custom User model and custom admin class
admin.site.register(User, CustomUserAdmin)

# Optional: Register any groups (e.g., Admin Group)
admin.site.unregister(Group)  # Unregister the default Group model
