from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'gender', 'address', 'location', 'age', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'gender', 'address', 'location', 'age', 'role')}),
    )
admin.site.register(User, CustomUserAdmin)
# Register your models here.

# admin.site.register(User)
