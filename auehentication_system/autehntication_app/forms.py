from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
	"""
	"""
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
					'username',
					'first_name',
					'last_name',
					'email',
					'password1',
					'password2'
		)


class CustomUserChangeForm(UserChangeForm):
	"""
	"""
	#email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
					'username',
					'first_name',
					'last_name',
					'email',
					'password'
		)

