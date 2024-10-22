from django.contrib import admin

from .models import Transaction

 
@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
 list_display = ('user','tx_type')
 
 search_fields = ['user','tx_type']
 
 list_filter = ('user','tx_type')
 
 