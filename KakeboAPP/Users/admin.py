from django.contrib import admin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff']
    search_fields = ['username', 'email']
    list_filter = ['user_type', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'user_type', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    ordering = ['email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'avatar']
    search_fields = ['user__username', 'bio']
    list_filter = ['user__username']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)