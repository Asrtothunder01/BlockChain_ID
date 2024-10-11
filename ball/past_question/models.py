import uuid
from django.db import models
from question.models import Question

from django.core.validators import FileValidator




class BaseModel(models.Model):
    id = models.UUIDField(Unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True




class Subject (BaseModel):
   
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
        


class Exam(BaseModel):
	name = models.CharField(max_length = 255)
	
	subject = models.ForeignKey(on_delete = models.CASCADE, Subject, unique = True)
	
	def __str__(self):
		return self.name



class QuestionPaper(BaseModel):
    
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    
    pdf_file = models.FileField(upload_to = 'question_papers/', validators =[ FileValidator(max_size = 10*1024*1024)])
    
    academic_session = models.IntegerField()
    
    def __str__(self):
        return f"{self.question}-{self.academic_session}"