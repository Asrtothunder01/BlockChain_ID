from rest_framework import serializers
from report.models import Report

class ReportSerializer (serializers.ModelSerializer):
	answer = AnswerSerializer (many =True)
	question = QuestionPaperSerializer (many = True)
	user = UserSerializer (many = True)
	class Meta:
		model = Report
		fields = ['id','user','question','answer','report_response']
		read_only_fields = ['id','user']