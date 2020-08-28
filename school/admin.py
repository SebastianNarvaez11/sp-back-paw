from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Grade

# Register your models here.


class GradeResource(resources.ModelResource):
    class Meta:
        model = Grade


class GradeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = GradeResource

admin.site.register(Grade,GradeAdmin)