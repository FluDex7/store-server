from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'is_active')
    search_fields = ('username',)
    list_filter = ('is_active','is_staff')
    inlines = (BasketAdmin,)