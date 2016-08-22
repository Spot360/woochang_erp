from django.conf.urls import url
from . import views

urlpatterns = [	
	url(r'^$', views.index),
	url(r'^about/$', views.about),
	url(r'^service_3PL/$', views.service_3PL),
	url(r'^service_IT/$', views.service_IT),
	url(r'^contactus/$', views.contactus),
]
