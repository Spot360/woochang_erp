from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
	customer = models.ForeignKey(User)
	material_name = models.CharField(max_length = 128)
	material_code = models.CharField(max_length = 20)
	control_code = models.CharField(max_length = 20)
	unit = models.CharField(max_length = 10, default = 'BOX')
	memo = models.TextField(blank = True)
	
	def __str__(self):
		return '{} ( {} [{}] )'.format(self.customer.username,self.material_name,self.material_code)

class Pallet(models.Model):
	pallet = models.CharField(max_length = 20)

	def __str__(self):
		return self.pallet

class Zone(models.Model):
	zone = models.CharField(max_length = 20)

	def __str__(self):
		return self.zone

class Outgoing(models.Model):
	pallet = models.ForeignKey(Pallet)
	material = models.ForeignKey(Material)
	outgoing_date = models.DateTimeField('date outgoing')
	outgoing_count = models.IntegerField(default = 0)
	zone = models.ForeignKey(Zone)
	
	def __str__(self):
		return '{} {}'.format(self.outgoing_date, self.material)

class Incoming(models.Model):
	pallet = models.ForeignKey(Pallet)
	material = models.ForeignKey(Material)
	incoming_date = models.DateTimeField('date incoming')
	incoming_count = models.IntegerField(default = 0)
	zone = models.ForeignKey(Zone)

	def __str__(self):
		return '{} {}'.format(self.incoming_date, self.material)
