from rest_framework import serializers
from .models import Subject,QuestionPaper,Exam


# SubjectSerializer
class SubjectSerializer (serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields =['id','name']
        read_only_fields = ['id']



# Exam Serializer
class Exam (serializers.ModelSerializer):
                subject = SubjectSerializer ()
                class Meta:
                	model = Exam
                	fields = ['id','subject',' name']
                	read_only_fields = ['id']
                
        
# QuestionPaper

class QuestionPaperSerializer(serializer.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields= ['id','question','pdf','academic_session']
        read_only_fields = ['id']