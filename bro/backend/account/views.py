from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

from drf_spectacular.utils import extend_schema

from .models import User


@extend_schema(
 tags = ['User'],
 responses = {201: UserSerializer (many = False)},
)

class UserCreateView (CreateAPIView):
    
    queryset = User.objects.all()
    
    serializer_class = UserSerializer
    
    pagination_class = None
    
    permission_classes = [IsAuthenticated]
    
    
@extend_schema(
  tags = ['User'],
  responses = {200:UserSerializer(many = True
)},
)

class UserListView(ListAPIView):
    
    queryset = User.objects.all()
    
    serializer_class = UserSerializer
    
    pagination_class = None
    
    permission_classes = [IsAuthenticated]