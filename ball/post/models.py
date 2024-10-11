from django.db import models
from discussion.models import Discussion
from account.models import User
# Create your models here.
class Post(models.Model):
	
	id = models.UUIDField(unique = True, editable = False, primary_key = True, default = uuid.uuid4)
	
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	
	discussion = models.ForeignKey(Discussion,on_delete = models.CASCADE)
	
	content = models.TextField(blank = True)
	
	def __str__(self):
	    return self.discussion
