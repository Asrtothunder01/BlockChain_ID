from rest_framework import serializers

from .models import User

class UserSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = User
        
        fields = ['id','name','email','dob','blockchain_address','created_at','updated_at']
        
        read_only_fields = ['id','created_at','updated_at']
        
        