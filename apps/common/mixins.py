from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import utils


class NameMixin(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RelatedObjectMixin(models.Model):

    class Meta:
        abstract = True

    @property
    def related_objects_model_name(self):
        try:
            return utils.get_model_name(self.related_objects[0])
        except IndexError:
            return ''

    @property
    def related_objects_ids(self):
        try:
            return self.related_objects.values_list('id', flat=True)
        except AttributeError:
            return [item.id for item in self.related_objects]
