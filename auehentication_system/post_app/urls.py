from django.conf.urls import include, url
from .views import HomeTemplate
from . import views
# from django.contrib.auth.views import (login, 
#     logout ,
#     password_reset,
#     password_reset_done,
#     password_reset_confirm,
#     password_reset_complete,
#     )

urlpatterns = [
    # Examples:
    # url(r'^$', 'auehentication_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeTemplate.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')

    ]