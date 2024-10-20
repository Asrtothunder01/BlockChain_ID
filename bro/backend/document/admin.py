from django.db import admin

from .models import Document

@admin.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user','document_type')
    
    list_filter = ('user','document_type')
    
    search_fields = ('user__username','document_type')
    
    date_hierarchy = 'upload_at'
    