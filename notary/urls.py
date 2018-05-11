from django.conf.urls import include, url
from django.conf import settings

from notary.views import home, about
from profile.views import auth, register, user_logout


urlpatterns = [
    # common views..
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    # userprofile stuff..
    url(r'^login/$', auth, name='login'),
    url(r'^register/$', register, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
]