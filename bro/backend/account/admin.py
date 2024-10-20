from django.db import admin

from .models import User

@admin.register(User)

class UserAdmin (admin.ModelAdmin):
    list_display = ('name','email','status')
    
    list_filter = ('name','email')
    
    date_hierarchy = 'created_at'
    
    search_fields = ('name','email')