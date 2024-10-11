from django.db import models
from answer.models import Answer
from question.models import Question
from account.models import User
# Create your models here.
class Report(models.Model):
	id = models.UUIDField(unique = True, editable = False, primary_key = True, default = uuid.uuid4)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	answer = models.ForeignKey(Answer,on_delete = models.CASCADE)
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	report_response = models.TextField(blank = True)
	created_at = models.DateTimeField(auto_now = True)