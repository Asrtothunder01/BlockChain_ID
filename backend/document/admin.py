from django.contrib import admin

from .models import Document

 
@admin.register(Document)

class DocumentAdmin(admin.ModelAdmin):
 list_display = ('document_type','document_location')
 
 search_fields = ('document_type','document_location')
 
 date_hierarchy = 'upload_at'
 
 list_filter = ('document_location','document_type')
 
 