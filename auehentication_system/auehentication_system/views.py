from django.shortcuts import render, redirect

def redirect_login(request):
	"""
	"""
	
	return redirect('/auth_sys/login')
