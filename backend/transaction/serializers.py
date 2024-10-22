from rest_framework import serializers

from .models import Transaction

from account.models import User

class TransactionSerializer(serializers.ModelSerializer):
    
    user = UserSerializer (read_only = True)
    
    class Meta:
        model = Transaction
        
        fields = ['id','user','blockchain_address','tx_type','created_at','updated_at']
        
        read_only = ['id','user','created_at','updated_at']