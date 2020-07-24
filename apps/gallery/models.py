from typing import List

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.common import mixins, utils


class CommonPhotoManager(models.Manager):

    def update_status_by_id(self, list_id: List or int or str, is_approve: bool) -> int:
        list_with_id = []

        if type(list_id) == list:
            list_with_id = list_id

        if type(list_id) == str or type(list_id) == int:
            list_with_id.append(list_id)

        return self.get_queryset().filter(id__in=list_with_id).update(is_approved=is_approve)

    def get_instance_photo(self, instance):
        """Get all photo instance, for example get all thing table photo"""
        return self.get_queryset().filter(
            content_type__model=utils.get_model_name(instance),
            object_id=instance.pk,
        )

    def get_instance_type_photo(self, instance):
        """Get all photo instance, for example get all country photo"""
        return self.get_queryset().filter(
            content_type__model=utils.get_model_name(instance),
        )

    def get_photo_by_instance_model_name(self, name):
        """Get all photo instance, for example get all city photo by name='city"""
        return self.get_queryset().filter(
            content_type__model=name.lower(),
        )

    def get_photo_in_country(self, country):
        """Get all country photo and all photo in country"""
        return self.get_queryset().filter(
            Q(location__country=country) |
            Q(content_type__model=utils.get_model_name(country), object_id=country.pk,)
        )

    def get_photo_related_models(self, instance):
        """Get photos related models"""
        if not instance.has_related_object:
            return self.get_queryset().none()
        return self.get_queryset().filter(
            content_type__model=instance.related_objects_model_name,
            object_id__in=instance.related_objects_ids,
        )


class UnapprovedPhotoManager(CommonPhotoManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=False)

    def set_approve_photo_by_id(self, list_id: List or int or str) -> int:
        """Change status photo with id in list_id or id equal list_id on approved"""
        return self.update_status_by_id(list_id, is_approve=True)


class ApprovedPhotoManager(CommonPhotoManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)

    def unset_approve_photo_by_id(self, list_id: List or int or str) -> int:
        """Change status photo with id in list_id or id equal list_id on unapproved"""
        return self.update_status_by_id(list_id, is_approve=False)


class Photo(mixins.NameMixin):
    author = models.ForeignKey(
        get_user_model(),
        related_name='photos',
        verbose_name=_('Author'),
        on_delete=models.CASCADE
    )
    image = models.ImageField(_('Image'), upload_to="photos/%Y/%m/%d")
    location = models.ForeignKey(
        'geo.City',
        verbose_name=_('City'),
        related_name='photos',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_('Created at'), default=timezone.now)
    modified_at = models.DateTimeField(_('Modified at'), auto_now=True)
    is_approved = models.BooleanField(verbose_name=_('Approved'), default=False,)
    content_type = models.ForeignKey(
        ContentType,
        models.CASCADE,
        verbose_name=_('Content type'),
    )
    object_id = models.PositiveIntegerField(verbose_name=_('Object ID'), null=True,)
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = models.Manager()
    common = CommonPhotoManager()
    approved = ApprovedPhotoManager()
    unapproved = UnapprovedPhotoManager()

    class Meta:
        db_table = 'photos'
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
