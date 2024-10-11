from  django.contrib import admin
from . models import Subject, Exam,QuestionPaper

@admin.register(Subject)

class SubjectAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
	list_display = ('name','subject')
	search_fields = ['name','subject']
	
@admin.register(QuestionPaper)

class QuestionPaperAdmin(admin.ModelAdmin):
	list_display = ('question','academic_session')
	search_fields = ['question','academic_session']