import uuid

from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        
class User(models.Model):
   
   USER_STATUS = (
   ('Pending','Pending'),
   ('Verified','Verified'),
   ('Failed','Failed'),
      
   )
   
   blockchain_address = models.CharField(max_length = 50)
   
   name = models.CharField(max_length = 25)
   
   email = models.EmailField(unique = True)
   
   status = models.CharField(max_length = 25, choices = USER_STATUS, default = 'Pending')
   
   def __str__(self):
       return self.name