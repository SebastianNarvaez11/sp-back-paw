from django.db import models
from base.softdelete import SoftDeletionManager
from base.utils import get_guid
from django_userforeignkey.models.fields import UserForeignKey

class Base(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=40, verbose_name="ID")
    deleted = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user_create = UserForeignKey(auto_user_add=True, related_name='+')
    user_update = UserForeignKey(auto_user=True, related_name='+')

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)
    
    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, update_fields=None, using=None, request=None): 
        is_new = False
        if not self.id:
            is_new = True
            self.id = get_guid()
        super(Base, self).save(force_insert, force_update, using, update_fields)