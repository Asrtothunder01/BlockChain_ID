from django.db import models
from discussion.models import Discussion
from account.models import User
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	discussion = models.ForeignKey(Discussion,on_delete = models.CASCADE)
	content = models.TextField(blank = True)
