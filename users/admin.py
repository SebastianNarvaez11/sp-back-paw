from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Admin, User, Student

# Register your models here.
class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource

admin.site.register(Admin)
admin.site.register(User, UsersAdmin)
admin.site.register(Student)