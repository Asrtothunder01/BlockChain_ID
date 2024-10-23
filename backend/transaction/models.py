import uuid

from account.models import User

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        
   
class Transaction(BaseModel):
    
    TX_TYPE = (
    ('Register','Register'),
    ('Verify','Verify'),    
    ('Failed','Failed'),
    
    )
    
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    tx_type = models.CharField(max_length = 25, choices = TX_TYPE, default = 'Pending')
    
    blockchain_tx_hash = models.CharField(max_length = 50)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.user