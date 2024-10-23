import uuid

from account.models import User

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        
   
class Document(BaseModel):
    
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    document_type = models.CharField(upload_to = 'document/')
    
    document_hash = models.CharField(max_length = 50)
    
    upload_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.user