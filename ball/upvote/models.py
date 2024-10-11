from django.db import models
from  question.models import Question
from answer.models import Answer
# Create your models here.
class Upvote(models.Model):
	user = models.ForeignKey(Question,on_delete = models.CASCADE)
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	answer  = models.ForeignKey(Answer,on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now = True)