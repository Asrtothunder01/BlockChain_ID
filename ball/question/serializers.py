from .models import Question
from rest_framework import serializers

class QuestionSerializer (serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ['id','user','academic_session','question_text','updated_at','created_at']
		