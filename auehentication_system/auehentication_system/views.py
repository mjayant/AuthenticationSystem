from django.shortcuts import render, redirect
from django.contrib import messages


def redirect_login(request):
	"""
	"""
	
	return redirect('/auth_sys/login')
