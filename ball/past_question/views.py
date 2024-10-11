from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import QuestionPaper, Subject,Exam

from .serializer import SubjectSerializer, QuestionPaperSerializer, ExamSerializer

from rest_framework.exceptions import APIEXCEPTION

from rest_framework.response import Response

from rest_framework import status

from drf_spectacular.utils import extend_schema
 
from drf_spectacular.types import OpenApiTypes




# Subject View

''' SUBJECTAPIVIEW '''

@extend_schema(
tags = ['Subject'],
responses = {200: SubjectSerializer (many = True)},
)
class SubjectListView(ListAPIView):
         queryset = Subject.objects.all()
         
         serializer_class = SubjectSerializer
    
         permission_classes = [IsAuthenticated]
    
         pagination_class = None

        
@extend_schema(
  tags = ['Subject'],
  responses = {201: SubjectSerializer (many = True)},
)        
class SubjectCreateView(CreateAPIView):
         queryset = Subject.objects.all()
         
         serializer_class = SubjectSerializer
    
         permission_classes = [IsAuthenticated]
    
         pagination_class = None
    
    
    
# Exam View

''' EXAMAPIVIEW '''


@extend_schema(
  tags = ['Exam'],
  responses = {200:ExamSerializer(many = True)},
)     

class ExamListView(ListAPIView):
         
         queryset = Exam.objects.all()
         
         serializer_class = ExamSerializer
    
         permission_classes = [IsAuthenticated]
    
         pagination_class = None
         
         
         
@extend_schema(
  tags = ['Exam'],
  responses = {201: ExamSerializer( many = True)},
)
class ExamCreateView(CreateAPIView):
         queryset = Exam.objects.all()
         
         serializer_class = ExamSerializer
    
         permission_classes = [IsAuthenticated]
    
         pagination_class = None

        
                
                                
 # QuestionPaper View 
 
''' QUESTIONPAPERVIEW '''
 
 
@extend_schema(
  tags = ['QuestionPaper'],
  responses = {200: QuestionPaperSerializer (many = True)},
) 
     
class QuestionPaperListView(ListAPIView):
    
         queryset = QuestionPaper.objects.all()
         
         serializer_class = QuestionPaperSerializer
    
         permission_classes = [IsAuthenticated]
    
         pagination_class = None
    
    
@extend_schema(
 tags =['QuestionPaper'],
 responses = {201: QuestionPaperSerializer(many = True)},
)
class QuestionPaperCreateView(CreateAPIView):
         
         queryset = QuestionPaper.objects.all()
         
         serializer_class = QuestionPaperSerializer
    
         permission_classes = [IsAuthenticated]
    
         pagination_class = None
         
    
         def create(self,request,*args,**Kwargs):            
            if request.method == 'POST':
               try:
                  file = request.FILES.get('pdf_file', None)
                  if not file:
                  	return Response({'detail':'No File Provided'}, status = status.HTTP_400_BAD_REQUEST)
                  if file.size > 10*1024*1024:
                      return Response ({'detail':'file size exceeds 10MB limit'}, status =status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
                  response = super().create(request,*args,**Kwargs)
                  return Response ({'detail':'file uploaded successfully'},status = status.HTTP_201_CREATED)              
               except Exception as e:
                    return Response({'Error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)  
                    
                  
            
            
        
        
    