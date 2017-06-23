import re
from django.conf import settings
from django.shortcuts import redirect


url_complie_regex = [re.compile(url) for url in settings.ALLOW_URLS]
class LoginMiddleware(object):
	"""
	"""
	def process_view(self, request, view_func, view_args, view_kwargs):
		"""
		"""
		#import pdb ;pdb.set_trace()
		print request.path
		print request.path.lstrip('/').rstrip('/')
		#import pdb ;pdb.set_trace()
		if not request.user.is_authenticated()   and not any( [item.match(request.path.lstrip('/').rstrip('/')) for item in url_complie_regex]):
			return redirect(settings.LOGIN_URL)
		elif request.user.is_authenticated() and any( item.match(request.path) for item in url_complie_regex):
			return redirect('/auth_sys/')
		else:
			return None