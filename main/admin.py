from django.contrib import admin
from .models import User, Contact
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['email', 'active']
    search_fields = ['email']
    list_filter  = ['active']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created']
    search_fields = ['name', 'email', 'body']
    ordering = ['created']