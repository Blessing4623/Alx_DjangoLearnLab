from django import forms
from .models import Profile, Post, Comment
from taggit.forms import TagWidget
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget()
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']