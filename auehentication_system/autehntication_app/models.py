from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class UserProfile(models.Model):
	"""
	"""
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100)
	website = models.URLField()
	birth_date = models.DateField(auto_now_add=True)
	city = models.CharField(max_length=50)
	image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, max_length=500)

	def __str__(self):
		"""
		"""
		return self.user.username


def save_profile(sender, **kwargs):
	"""
	"""
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(save_profile, sender=User)