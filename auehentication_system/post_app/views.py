from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import PostForm
from .models import Post, Friend
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your views here.

class HomeTemplate(TemplateView):
	"""
	"""

	def get(self, request):
		"""
		"""
		context = {}
		context['form'] = PostForm()
		post_data = Post.objects.all().order_by('-created')
		context['post_data'] = post_data
		user_lst = User.objects.all().exclude(id=request.user.id)

		try:
			friend_id = Friend.objects.get(current_user=request.user)
			friends = friend_id.users.all()
		except Friend.DoesNotExist:
			friends = set()

		context['friends'] = friends

		user_lst = set(user_lst) - set(friends)
		context['user_lst'] = user_lst
		return render(request, 'home.html', context)

	def post(self, request):
		"""
		"""
		form = PostForm(request.POST or None, request.FILES or None)
		#form = myForm(request.POST or None, request.FILES or None)
		text = ''
		context = {'form':form}
		#import pdb ;pdb.set_trace()
		if form.is_valid():
			text = form.cleaned_data['post']
			post = form.save(commit=False)
			post.user = request.user
			#import pdb ;pdb.set_trace()
			post.save()
			
			return redirect(reverse('home'))

			#return reverse('home')
		# else:
		#  	messages.error(request, "Error")
		
		return render(request,'home.html', context)


def change_friends(request, operation, pk):
	"""
	"""
	if operation == 'add':
		friend = User.objects.get(pk=pk)
		Friend.make_friend(request.user, friend)
	else:

		friend = User.objects.get(pk=pk)
		Friend.lose_friend(request.user, friend)
	return redirect(reverse('home'))	

