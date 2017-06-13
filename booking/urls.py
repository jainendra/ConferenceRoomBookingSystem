from django.conf.urls import url
from views import index, signup, login, logout, home


app_name = 'booking'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
