from rest_framework import serializers

from account.models import User

from .models import Document


class DocumentSerializer (serializers.ModelSerializer):
    
    user = UserSerializer (read_only = True)
    
    class Meta:
        model = Document
        
        fields = ['id','user','document_hash','document_location','document_type','upload_at','created_at','updated_at']
        
        read_only_fields = ['id','user','created_at','updated_at']

