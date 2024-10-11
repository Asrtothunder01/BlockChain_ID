from rest_framework import serializers
from .models import Discussion

class DiscussionSerializer(serializers.ModelSerializer):
	user = UserSerializer (many = True)
	class Meta:
		model = Discussion
		fields = ['id','user','title', 'body']
		read_only_fields = ['id','user']