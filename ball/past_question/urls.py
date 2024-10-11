from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
  
  path('subject/v1/',views.SubjectListView.as_view(), name = 'Subject_list'),
  path('subject/v2/',views.SubjectCreateView.as_view(), name = 'subject_create'),
  path('exam/v1/',views.ExamListView.as_view(), name = 'exam_list'),
  path('exam/v2/',views.ExamCreateView.as_View(),name = 'exam_create'),
  path('paper/v1/',views.QuestionPaperListView.as_view(), name = 'QuestionPaper_list'),
  path('paper/v2/',views.QuestionPaperCreateView.as_view(),name = 'QuestionPaper_create'),

]