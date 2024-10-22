from django.contrib import admin

from .models import User

 
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
 list_display = ('name','status','dob')
 
 search_fields = ['name','status__dob']
 
 list_filter = ('name','status')
 
 