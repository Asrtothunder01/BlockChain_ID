from rest_framework import serializers
from .models import Post

class PostSerializer (serializers.ModelSerializer):
	user = UserSerializer (many = True)
	discussion = DiscussionSerializer (many = True)
	class Meta:
		model = Post
		fields = ['id','user','discussion','content']
		read_only_fields = ['id','user']