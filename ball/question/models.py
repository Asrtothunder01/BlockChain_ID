from django.db import models
from account.models import User
# Create your models here.

class Question(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	academic_session = models.IntegerField(default = 0)
	question_text = models.TextField(blank = True)
	updated_at = models.DateTimeField(auto_now = True)
	created_at  = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.question_text[:50]