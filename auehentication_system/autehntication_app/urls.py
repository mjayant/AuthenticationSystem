from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import (login, 
    logout ,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    )

urlpatterns = [
    # Examples:
    # url(r'^$', 'auehentication_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name':'login.html'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^viewprofile/$',views.view_profile, name='view_profile'),
    url(r'^editprofile/$',views.edit_profile, name='edit_profilee'),
    url(r'^editprofile/password/$',views.changePassword, name='changePassword'),
    url(r'^forgotpassword/$',password_reset, name='forgotpassword'),
    url(r'^forgotpassword/done$',password_reset_done, name='password_reset_done'),
    url(r'^passwordresetconfirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',password_reset_confirm, name='password_reset_confirm'),
    url(r'^passwordresetconfirm/complete$',password_reset_complete, name='password_reset_complete'),    

]

