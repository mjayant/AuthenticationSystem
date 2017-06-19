from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
# Create your views here.


def home(request):
	"""
	"""
	return render(request, 'home.html', {})

def register(request):
	"""
	"""
	form = CustomUserCreationForm(request.POST or None, request.FILES or None)
	context = {}
	context['form'] = form
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/auth_sys/login')
	else:
		messages.error(request, "Error")

	return render(request, 'register.html', context)



def view_profile(request):
	"""
	"""
	#import pdb ;pdb.set_trace()
	if  request.method == 'POST':
		return redirect('/auth_sys/editprofile')
	return render(request, 'view_profile.html',{})

def edit_profile(request):
	"""
	"""
	context = {}
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		context['form'] = form
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('/auth_sys/viewprofile')
		else:
			messages.error(request, "Error")
	else:
		form = CustomUserChangeForm(instance=request.user)
		context['form'] = form

	return render(request, 'edit_profilee.html',context)	