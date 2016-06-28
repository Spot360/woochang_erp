from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Material)
admin.site.register(Pallet)
admin.site.register(Zone)
admin.site.register(Outgoing)
admin.site.register(Incoming)
