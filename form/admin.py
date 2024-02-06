# admin.py

from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['title', 'first_name', 'last_name', 'position', 'company', 'business', 'employees',
                    'street', 'additional', 'zipcode', 'place', 'country', 'code', 'phone', 'your_email', 'accept_terms']
    search_fields = ['first_name', 'last_name', 'company', 'phone', 'your_email']
    list_filter = ['position', 'business', 'employees', 'place', 'country']

admin.site.register(Registration, RegistrationAdmin)
