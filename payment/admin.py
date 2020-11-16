from django.contrib import admin
from .models import Payment, CompromisePay

# Register your models here.
admin.site.register(Payment)
admin.site.register(CompromisePay)
