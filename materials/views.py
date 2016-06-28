from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

# Create your views here.
from .models import Material

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
