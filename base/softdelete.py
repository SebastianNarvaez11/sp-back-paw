from django.db import models
from django.db.models.query import QuerySet

class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        # Bulk delete bypasses individual objects' delete methods.
        return super(SoftDeletionQuerySet, self).update(deleted=True)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted=False)

    def dead(self):
        return self.exclude(deleted=False)


class SoftDeletionManager(models.Manager):
    use_for_related_fields = True

    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        qset = SoftDeletionQuerySet(self.model)

        if self.alive_only:
            return qset.filter(deleted=False)
        return qset

    def hard_delete(self):
        return self.get_queryset().hard_delete()
