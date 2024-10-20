from django.contrib admin

from .models import Verifier,Verify

@admin.register(Verifier)

class VerifierAdmin(admin.ModelAdmin):
    list_display = ('name','verified_at')
    
    list_filter = ('name','verified_at')
    
    date_hierarchy = 'verified_at'
    
@admin.register(Verify):
    
class VerifyAdmin(admin.ModelAdmin):
    
    list_display = ('user','verifier')
    
    list_filter = ('user','verifer')
    