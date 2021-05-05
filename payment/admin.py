from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Payment, CompromisePay

# Register your models here.


class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment


class PaymentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = PaymentResource


class CompromiseResource(resources.ModelResource):
    class Meta:
        model = CompromisePay()


class CompromiseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = CompromiseResource


admin.site.register(Payment, PaymentAdmin)
admin.site.register(CompromisePay, CompromiseAdmin)
