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
		# customer_list = Customer.objects.all()
	except:
	 	raise Http404('Nothing information')
	# customer_name = []
	# for incoming in incoming_list:
	# 	customer_id = incoming.material.customer.id
	# 	customer = Customer.objects.filter(user_id=customer_id)
	# 	customer_name += customer
	# print('@@@@@@@@@@@@@@@@@@@@@@', customer_name)
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)
	
def incoming_material(request, material_id):
	try:
		material = Material.objects.get(id=material_id)
	except:
		raise Http404('Nothing information')
	incoming_list = material.incoming_set.all().order_by('material')
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_pallet(request, pallet_id):
	try:
		pallet = Pallet.objects.get(id=pallet_id)
	except:
		raise Http404('Nothing information')
	incoming_list = pallet.incoming_set.all().order_by('material')
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_zone(request, zone_id):
	try:
		zone = Zone.objects.get(id = zone_id)
		pallets = zone.pallet_set.all()
	except:
		raise Http404('Nothing information')
	pallet_id = []
	for pallet in pallets:
		pallet_id.append(pallet.id)
	incoming_list = []
	for id in pallet_id:
		incoming = Incoming.objects.filter(pallet_id = id)
		incoming_list += incoming
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_customer(request, customer_id):
	try:
		customer = Customer.objects.get(id=customer_id)
		materials = customer.material_set.all()
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

def outgoing(request):
	try:
		outgoing_list = Outgoing.objects.all().order_by('outgoing_date')
	except:
	 	raise Http404('Nothing information')
	context = {'outgoing_list':outgoing_list}
	return render(request, 'materials/outgoing.html', context)

def outgoing_detail(request, customer_id):
	# material_list = get_object_or_404(Material, pk=customer_id)
	material_list = Material.objects.get(pk=customer_id)
	context = {'material_list':material_list}
	return render(request, 'materials/outgoing_detail.html', context)

	# return HttpResponse("Star WooChang Material ERP")

def submit(request):
	return HttpResponse("Star WooChang Material ERP")

def result(request):
	incoming_list = Incoming.objects.all()
	outgoing_list = Outgoing.objects.all()
	material_list = Material.objects.all()
	packing_list = Packing.objects.all()
	material_id = []
	for material in material_list:
		material_id.append(material.id)
	
	count_result = []
	for id in material_id:
		result={}
		for packing in packing_list:
			incoming_counts = Incoming.objects.filter(material_id=id, packing_id=packing.id).aggregate(Sum('incoming_count'))
			result[packing.Packing_code] = incoming_counts['incoming_count__sum']
			


	

	return render(request, 'materials/result.html', context)
