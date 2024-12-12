from rest_framework import serializers
from .models import Post, Comment, Like
# creating a whole lot of serializers here 
# well enjoy the code


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= "__all__"
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"