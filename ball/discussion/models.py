from django.db import models
from account.models import User
# Create your models here.
class Discussion(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	title = models.CharField(max_length = 255, blank = True)
	body = models.TextField(blank = True)
	def __str__(self):
		return self.title