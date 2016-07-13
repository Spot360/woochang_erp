from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^c/([0-9]+)/$', views.index_detail, name='index_c'),

	url(r'^incoming/$', views.incoming, name='incoming'),
	url(r'^incoming/p/([0-9]+)/$', views.incoming_pallet, name="incoming_p"),
	url(r'^incoming/c/([0-9]+)/$', views.incoming_customer, name="incoming_c"),
	url(r'^incoming/z/([0-9]+)/$', views.incoming_zone, name="incoming_z"),
	url(r'^incoming/m/([0-9]+)/$', views.incoming_material, name="incoming_m"),
	
	url(r'^outgoing/$', views.outgoing, name='outgoing'),
	url(r'^outgoing/p/([0-9]+)/$', views.outgoing_pallet, name="outgoing_p"),
	url(r'^outgoing/c/([0-9]+)/$', views.outgoing_customer, name="outgoing_c"),
	url(r'^outgoing/z/([0-9]+)/$', views.outgoing_zone, name="outgoing_z"),
	url(r'^outgoing/m/([0-9]+)/$', views.outgoing_material, name="outgoing_m"),

	url(r'^result/$', views.result, name='result'),
	# url(r'^outgoing/$', views.OutgoingList.as_view(), name='outgoing_list'),
	
	# url(r'^material/(?P<pk>\d+)/$', views.MaterialDetail.as_view(), name='material_detail'),
	# url(r'^incoming/(?P<pk>\d+)/$', views.IncomingDetail.as_view(), name='incoming_detail'),
	# url(r'^outgoing/(?P<pk>\d+)/$', views.OutgoingDetail.as_view(), name='outgoing_detail'),

	# url(r'^outgoing/(?P<customer_id>\d+)/$', views.outgoing_detail, name='detail'),
	# url(r'^outgoing/(?P<customers>)/submit/$', views.submit, name='submit'),
	# url(r'^outgoing/(?P<customers>)/result/$', views.result, name='result'),
]
