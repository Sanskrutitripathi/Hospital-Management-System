from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(appointment)
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(staff)
admin.site.register(historie)