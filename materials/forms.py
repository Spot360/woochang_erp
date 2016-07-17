from django import forms
from django.forms import ModelForm
from .models import *

# class outgoingForm(forms.Form):
# 	zone = forms.CharField(label = 'Zone ID', max_length = 20)
# 	pallet = forms.CharField(label = 'Pallet ID', max_length = 20)
# 	material_code = forms.CharField(label ='Material Code', max_length = 20)
# 	unit = forms.CharField(label ='Unit', max_length = 10)
# 	count = forms.IntegerField(label ='Count')

class incomingForm(ModelForm):
	class Meta:
		model = Incoming
		fields = {'pallet', 'material', 'incoming_date', 'incoming_unit', 'incoming_count', 'unpackBox_count'}

class outgoingForm(ModelForm):
	class Meta:
		model = Outgoing
		fields = {'pallet', 'material', 'outgoing_date', 'outgoing_unit', 'packing', 'outgoing_count', 'unpackBox_count'}
		