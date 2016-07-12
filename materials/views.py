from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

# Create your views here.
from .models import *
from customers.models import *

def index(request):
	try:
		material_list = Material.objects.all().order_by('material_name').order_by('customer')
	except:
		raise Http404('Nothing material')
	context = {'material_list': material_list, 'customer':'Total',}
	return render(request, 'materials/index.html', context)

def index_detail(request, customer):
	try:
		user = User.objects.get(username=customer)
	except:
		raise Http404('Nothing material')
	material_list = user.material_set.all().order_by('material_name').order_by('customer')
	context = {'material_list': material_list,'customer':customer}
	return render(request, 'materials/index.html', context)

def incoming(request):
	try:
		incoming_list = Incoming.objects.all().order_by('incoming_date')
	except:
	 	raise Http404('Nothing incoming')
	customer_name = []
	for incoming in incoming_list:
		customer_id = incoming.material.customer.id
		customer = Customer.objects.filter(user_id=customer_id)
		customer_name += customer
	print('@@@@@@@@@@@@@@@@@@@@@@', customer_name)
	context = {'incoming_list':incoming_list, 'customer_name':customer_name}
	return render(request, 'materials/incoming.html', context)
	
def incoming_pallet(request, pallet_id):
	try:
		pallet = Pallet.objects.get(id=pallet_id)
	except:
		raise Http404('Nothing information')
	incoming_list = pallet.incoming_set.all().order_by('material')
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_customer(request, customer_id):
	try:
		user = User.objects.get(id=customer_id)
		materials = user.material_set.all()
	except:
		raise Http404('Nothing information')
	material_id =[]
	for material in materials:
		material_id.append(material.id)
	incoming_list = []
	for id in material_id:
		incoming = Incoming.objects.filter(material_id=id)
		incoming_list += incoming
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)


def outgoing_detail(request, customer_id):
	# material_list = get_object_or_404(Material, pk=customer_id)
	material_list = Material.objects.get(pk=customer_id)
	context = {'material_list':material_list}
	return render(request, 'materials/outgoing_detail.html', context)

	# return HttpResponse("Star WooChang Material ERP")

def submit(request):
	return HttpResponse("Star WooChang Material ERP")

def result(request):
	return HttpResponse("Star WooChang Material ERP")
