from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'active']
    search_fields = ['email']
    list_filter  = ['active']