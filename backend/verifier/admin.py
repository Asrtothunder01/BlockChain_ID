from django.contrib import admin

from .models import User

 
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
 list_display = ('name','blockchain_address')
 
 search_fields = ['name','blockchain_address']
 
 list_filter = ('name','blockchain_address')
 
 