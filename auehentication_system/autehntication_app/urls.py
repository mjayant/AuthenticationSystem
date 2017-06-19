from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout 

urlpatterns = [
    # Examples:
    # url(r'^$', 'auehentication_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name':'login.html'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^register/$',views.register, name='register'),
    url(r'^viewprofile/$',views.view_profile, name='view_profile'),
    url(r'^editprofile/$',views.edit_profile, name='edit_profilee'),

]