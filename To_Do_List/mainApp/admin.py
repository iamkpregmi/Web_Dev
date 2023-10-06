from django.contrib import admin
from .models import *

class to_do_data_Admin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'user')

class contactUs_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'desc', 'created_date')

admin.site.register(to_do_data,to_do_data_Admin)
admin.site.register(contactUs,contactUs_Admin)
