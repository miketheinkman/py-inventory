from django.conf.urls import url
from . import views


app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vendors$', views.vendors, name='vendors'),
    url(r'^listing/(?P<vendor>[a-zA-Z0-9]+)/$', views.listing, name='list_detail'),
    url(r'^email/(?P<vendor>[a-zA-Z0-9]+)/$', views.send_mail, name='email'),
    url(r'^email$', views.send_mail, name='email'),
    url(r'^listing$', views.listing, name='listing'),
    url(r'^remove$', views.remove, name='remove'),
    url(r'^add$', views.add, name='add'),
    url(r'^help$', views.help_page, name='help'),
    url(r'^logout$', views.logout_function, name='logout'),
]