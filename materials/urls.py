from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^c/(?P<customer>\w+)/$', views.index_detail, name='index'),

	# url(r'^material/$', views.MaterialList.as_view(), name='material_list'),
	url(r'^incoming/$', views.incoming, name='incoming'),
	url(r'^incoming/p/([0-9]+)/$', views.incoming_pallet, name="incoming_p"),
	url(r'^incoming/c/([0-9]+)/$', views.incoming_customer, name="incoming_c"),
	# url(r'^outgoing/$', views.OutgoingList.as_view(), name='outgoing_list'),
	
	# url(r'^material/(?P<pk>\d+)/$', views.MaterialDetail.as_view(), name='material_detail'),
	# url(r'^incoming/(?P<pk>\d+)/$', views.IncomingDetail.as_view(), name='incoming_detail'),
	# url(r'^outgoing/(?P<pk>\d+)/$', views.OutgoingDetail.as_view(), name='outgoing_detail'),

	# url(r'^outgoing/(?P<customer_id>\d+)/$', views.outgoing_detail, name='detail'),
	# url(r'^outgoing/(?P<customers>)/submit/$', views.submit, name='submit'),
	# url(r'^outgoing/(?P<customers>)/result/$', views.result, name='result'),
]
