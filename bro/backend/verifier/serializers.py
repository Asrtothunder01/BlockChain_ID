from rest_framework import serializers

from .models import Verifier, Verify

from account.models import User


class VerifierSerializer (serializers.ModelSerializer):

    
    class Meta:
        model = Verifier
        
        fields = ['id','name','blockchain_address','verified_at','created_at','updated_at']
        
        read_only_fields = ['id','created_at','updated_at']

                
class VerifySerializer(serializers.ModelSerializer):
        
        verifier = VerifierSerializer(read_only = True)
        user = UserSerializer (read_only = True)
                
        class Meta:
                        
            model = Verify
            
            fields = ['id','user','verify','status','blockchain_address','attempted_atq','verified_at','created_at','updated_at']
            
            read_only_fields = ['id','user','created_at','updated_at']

