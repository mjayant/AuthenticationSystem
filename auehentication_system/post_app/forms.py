from django import forms
from .models import Post


class PostForm(forms.ModelForm):

	post = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Write Post....'}))

	class Meta:
		model = Post
		fields = ('post',)

