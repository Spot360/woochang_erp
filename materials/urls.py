from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^c/(\d+)/$', views.index_detail, name='index_c'),

	url(r'^incoming/$', views.incoming, name='incoming'),
	url(r'^incoming/p(\d+)', views.incoming_pallet, name="incoming_p"),
	url(r'^incoming/c(\d+)', views.incoming_customer, name="incoming_c"),
	url(r'^incoming/z(\d+)', views.incoming_zone, name="incoming_z"),
	url(r'^incoming/m(\d+)', views.incoming_material, name="incoming_m"),

	url(r'^outgoing/$', views.outgoing, name='outgoing'),
	url(r'^outgoing/p(\d+)', views.outgoing_pallet, name="outgoing_p"),
	url(r'^outgoing/c(\d+)', views.outgoing_customer, name="outgoing_c"),
	url(r'^outgoing/z(\d+)', views.outgoing_zone, name="outgoing_z"),
	url(r'^outgoing/m(\d+)', views.outgoing_material, name="outgoing_m"),

	url(r'^result/$', views.result, name='result'),
	url(r'^result/c(\d+)', views.result, name='result_c'),
	url(r'^result/m(\d+)', views.result_detail, name='result_detail'),

	# url(r'^work/incoming/$', views.incoming_form.as_view(), name = 'work_incoming'),
	url(r'^work/incoming/$', views.incoming_form, name = 'work_incoming'),
	url(r'^incoming/edit(?P<pk>[0-9]+)', views.incoming_edit, name = 'work_incoming_edit'),
	# url(r'^work/outgoing/$', views.outgoing_form.as_view(), name = 'work_outgoing'),
	url(r'^work/outgoing/$', views.outgoing_form, name = 'work_outgoing'),
	url(r'^outgoing/edit(?P<pk>[0-9]+)', views.outgoing_edit, name = 'work_outgoing_edit'),

]
