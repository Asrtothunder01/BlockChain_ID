from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import ListAPIView, CreateAPIView

from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from drf_spectacular.types import OpenApiTypes
from .models import Discussion

from .serializers import DiscussionSerializer
# Create your views here.


@extend_schema(
  tags = ['Discussion'],
  responses = {200: DiscussionSerializer(many = True)},
)
class DiscussionListView(APIView):
    queryset = Discussion.objects.all()
    
    serializer_class = DiscussionSerializer
    
    permission_classes = [IsAuthenticated,]
    
    pagination_class = None
   
     
@extend_schema(
 tags = ['Discussion'],
 responses = {200: DiscussionSerializer (many = True)},
)

class DiscussionCreateView (CreateAPIView):
    queryset = Discussion.objects.all()
    
    serializer_class = DiscussionSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
