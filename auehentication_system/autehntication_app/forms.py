from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

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
					'password',

		)


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'city', 'image')