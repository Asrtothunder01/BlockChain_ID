import uuid

from account.models import User

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        
   
class Verifier (BaseModel):
    
    name = models.CharField(max_length = 25)
    
    blockchain_address = models.CharField(max_length = 50)
    
    
    verified_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

        
                        
class Verify (BaseModel):
    
    VERIFY_STATUS = (
     ('Pending','Pending'),
     
     ('Verified','Verified'),
     
     ('Failed','Failed'),
    
    )
    
    user = model.ForeignKey(User,on_delete = models.CASCADE)
    
    Verifier = models.ForeignKey(Verifier,on_delete = models.CASCADE)
    
    status = models.CharField(max_length = 25, choices = VERIFY_STATUS, default = 'Pending')
    
    blockchain_tx_hash = models.CharField(max_length = 25)
    
    attempted_at = Models.DateTimeField(auto_now_add = True)
    
    verified_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.user}x{self.status}"
    