import uuid

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        
   
class User(BaseModel):
    
    STATUS = (
   ('Pending','Pending'),
    ('Rejected','Rejected'),
    ('Verified','Verified'),    
    ('Failed','Failed'),
    
    )
    
    name = models.CharField(max_length =25)
    
    status = models.CharField(max_length = 25, choices = STATUS, default = 'Pending')
    
    blockchain_address = models.CharField(max_length = 50)
    
    dob = models.PositiveIntegerField(auto_now_add = True)
    
    def __str__(self):
        return self.user