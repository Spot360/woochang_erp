from django.conf.urls import url
from . import views

urlpatterns = [	
	url(r'^$', views.index),
	url(r'^about/$', views.about),
	url(r'^service_3pl/$', views.service_3pl),
	url(r'^service_it/$', views.service_it),
	url(r'^contactus/$', views.contactus),
	url(r'^account/$', views.account),
]
