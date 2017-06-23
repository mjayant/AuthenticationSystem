from django.conf.urls import include, url
from django.contrib import admin
from .views import redirect_login

urlpatterns = [
    # Examples:
    # url(r'^$', 'auehentication_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', redirect_login, name='redirect_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth_sys/', include('autehntication_app.urls')),
    #url(r'^accounts/profile/$',views.view_profile, name='view_profile'),
]
