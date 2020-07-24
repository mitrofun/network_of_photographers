from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common import mixins


class Country(mixins.NameMixin, mixins.RelatedObjectMixin):
    code2 = models.CharField(max_length=2, null=True, blank=True, unique=True)
    code3 = models.CharField(verbose_name='ISO3', max_length=3, null=True, blank=True, unique=True,)
    name = models.CharField(_('Name'), max_length=255, unique=True, db_index=True)

    class Meta:
        db_table = 'countries'
        ordering = ('name',)
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    @property
    def has_related_object(self) -> bool:
        return self.cities.count() > 0

    @property
    def related_objects(self):
        return self.cities.all()


class City(mixins.NameMixin, mixins.RelatedObjectMixin):
    country = models.ForeignKey('Country', related_name='cities', on_delete=models.CASCADE,)

    class Meta:
        db_table = 'city'
        verbose_name = _('City')
        verbose_name_plural = _('City')

    @property
    def has_related_object(self) -> bool:
        return self.things_in_city.count() > 0

    @property
    def related_objects(self):
        return [item.thing for item in self.things_in_city.all()]
