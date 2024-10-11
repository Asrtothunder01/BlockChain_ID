from rest_framework import serializers

from  upvote.models import Upvote

class UpvoteSerializer (serializers.ModelSerializer):
	
	question = QuestionPaperSerializer (many = True)
	answer = AnswerSerializer(many = True)
	
	user = UserSerializer(many = True)
	
	class Meta:
		
		model = Upvote
		
		fields =['id','user','question','answer']
		read_only_fields = ['id','user']