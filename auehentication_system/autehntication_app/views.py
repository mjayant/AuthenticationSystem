from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

# Create your views here.


def home(request):
	"""
	"""
	return render(request, 'home.html', {})

# def login(request):
# 	"""
# 	"""
# 	form = AuthenticationForm(request.POST or None)
# 	context = {}
# 	context['form'] = form
# 	if  request.method == 'POST':
# 		#import pdb ;pdb.set_trace()
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			instance.save()
# 			return redirect('/auth_sys')
# 		# else:
# 		# 	messages.error(request, "Error")
# 	else:

# 		if request.user.is_authenticated():
# 			redirect('/auth_sys')

# 	return render(request, 'login.html', context)

def register(request):
	"""
	"""
	form = CustomUserCreationForm(request.POST or None, request.FILES or None)
	context = {}
	context['form'] = form
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect(reverse('login'))
	else:
		messages.error(request, "Error")

	return render(request, 'register.html', context)


#@login_required
def view_profile(request):
	"""
	"""
	#import pdb ;pdb.set_trace()
	if  request.method == 'POST':
		return redirect(reverse('edit_profilee'))
		#return redirect('/auth_sys/editprofile')
	return render(request, 'view_profile.html',{})

#@login_required
def edit_profile(request):
    """
    """
    user_form = CustomUserChangeForm(instance=request.user)
    ProfileInlineFormSet = inlineformset_factory(User, UserProfile, fields=('website','city'))
    formset = ProfileInlineFormSet(instance=request.user)
    context = {}
    #import pdb ;pdb.set_trace()
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        formset = ProfileInlineFormSet(request.POST, request.FILES, instance=request.user)        
        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            formset = ProfileInlineFormSet(request.POST, request.FILES, instance=created_user)
 
            if formset.is_valid():
                created_user.save()
                formset.save()
                return redirect(reverse('view_profile'))
        else:
            messages.error(request, "Error")
    

    context['user_form'] = user_form
    context['formset'] = formset
    # else:
    #     form = CustomUserChangeForm(instance=request.user)
    #     context['form'] = form
    #     profile = UserProfile.objects.create(user=request.user)
    #     form1 = UserProfileForm(instance=profile)
    #     context['form1'] = form1

    return render(request, 'edit_profilee.html',context)

#@login_required
def  changePassword(request):
	"""
	"""
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		context['form'] = form
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('view_profile'))
			#return redirect('/auth_sys/viewprofile')
		else:
			messages.error(request, "Error")
	else:
		form = PasswordChangeForm(user=request.user)
		context['form'] = form

	return render(request, 'password_change.html',context)


