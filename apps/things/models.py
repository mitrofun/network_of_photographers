from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common import mixins


class Thing(mixins.NameMixin, mixins.RelatedObjectMixin):
    name = models.CharField(_('Name'), max_length=255, unique=True, db_index=True)

    class Meta:
        db_table = 'things'
        ordering = ('name',)
        verbose_name = _('Thing')
        verbose_name_plural = _('Things')

    @property
    def has_related_object(self) -> bool:
        return self.things_in_use.count() > 0

    @property
    def related_objects(self):
        return [item.user for item in self.things_in_use.all()]


class ThingInCity(models.Model):
    city = models.ForeignKey(
        'geo.City',
        verbose_name=_('City'),
        related_name='things_in_city',
        on_delete=models.CASCADE,
    )
    thing = models.ForeignKey(
        'things.Thing',
        verbose_name=_('Thing'),
        related_name='things_in_city',
        on_delete=models.CASCADE,
    )
    count = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'things_in_cities'
        verbose_name = _('Things in city')
        verbose_name_plural = _('Things in cities')

    def __str__(self):
        return f'{self.thing} in {self.city}'


class ThingInUse(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('User'),
        related_name='things_in_use',
        on_delete=models.CASCADE,
    )
    thing = models.ForeignKey(
        'things.Thing',
        verbose_name=_('Thing'),
        related_name='things_in_use',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'things_in_use'
        verbose_name = _('Thing in use')
        verbose_name_plural = _('Things in use')

    def __str__(self):
        return f'{self.thing} to {self.user}'
