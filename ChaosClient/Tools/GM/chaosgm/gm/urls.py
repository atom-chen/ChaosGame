from django.conf.urls import patterns, url
from gm import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
	url(r'^index$', views.index, name='homepage'),
]
