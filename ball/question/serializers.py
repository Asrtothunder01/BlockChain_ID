from .models import Question
from rest_framework import serializers

class QuestionSerializer (serializers.ModelSerializer):
	user = UserSerializer (many = True)
	class Meta:
		model = Question
		fields = ['id','user','academic_session','question_text','updated_at','created_at']
		read_only_fields = ['id','user']   
		
		