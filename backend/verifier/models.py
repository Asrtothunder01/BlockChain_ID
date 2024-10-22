import uuid

from account.models import User

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        
   
class Verifier(BaseModel):
    
    name = models.CharField(max_length = 50)
    
    blockchain_address = models.CharField(max_length = 50)
    
    verified_at = models.DateTimeField()
    
    
class verify(BaseModel):   
    
    STATUS = (
    ('Pending','Pending'),
    ('Registered','Registered')
    ('Verified','Verified'),    
    ('Failed','Failed'),
)
    
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    verifier = models.ForeignKey(Verifier,on_delete = models.CASCADE)
    
    status = models.CharField(max_length = 50, choices = STATUS, default = 'Pending')
    
    attempted_at = models.DateTimeField(auto_now = True)
    
    verified_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.user