from django.conf.urls import url
from views import signup, login, logout, home


app_name = 'booking'

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
