import pytest

from apps.gallery.models import Photo

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def unapproved_photo(photo_thing):
    photo_thing.is_approved = False
    photo_thing.save()
    return photo_thing


def test_managers_filter_approved(unapproved_photo, photo_country):

    assert Photo.common.count() == 2
    assert Photo.approved.count() == 1
    assert Photo.unapproved.count() == 1


@pytest.mark.parametrize('is_approve, expected', [
    [True, 1],
    [False, 0],
])
def test_update_status_photo_by_id(unapproved_photo, is_approve, expected):
    Photo.common.update_status_by_id(unapproved_photo.id, is_approve=is_approve)

    assert Photo.approved.count() == expected


def test_instance_photo(photo_user, user):

    assert Photo.common.get_instance_photo(user).count() == 1
    assert Photo.approved.get_instance_photo(user).count() == 1
    assert Photo.unapproved.get_instance_photo(user).count() == 0


def test_instance_type_photo(photo_user, photo_thing,
                             second_photo_thing, thing):

    assert Photo.common.get_instance_type_photo(thing).count() == 2
    assert Photo.approved.get_instance_type_photo(thing).count() == 2
    assert Photo.unapproved.get_instance_type_photo(thing).count() == 0


def test_photo_by_instance_model_name(photo_user, photo_thing, second_photo_thing):

    assert Photo.common.get_photo_by_instance_model_name('user').count() == 1
    assert Photo.approved.get_photo_by_instance_model_name('user').count() == 1
    assert Photo.unapproved.get_photo_by_instance_model_name('user').count() == 0


def test_photo_in_country(country, photo_country, photo_city, photo_thing):

    assert Photo.common.get_photo_in_country(country).count() == 3
    assert Photo.approved.get_photo_in_country(country).count() == 3


def test_photo_related_models_country(country, photo_city, photo_country, photo_user):

    assert Photo.common.get_photo_related_models(country).count() == 1
    assert photo_city in Photo.approved.get_photo_related_models(country)
    assert Photo.approved.get_photo_related_models(country).first().location.country_id == country.id


def test_photo_related_models_city(city, photo_city, photo_country, photo_thing, photo_user):

    assert Photo.common.get_photo_related_models(city).count() == 1
    assert photo_thing in Photo.approved.get_photo_related_models(city)


def test_photo_related_models_thing(thing, photo_city, photo_country, photo_thing, photo_user):

    assert Photo.common.get_photo_related_models(thing).count() == 1
    assert photo_user in Photo.approved.get_photo_related_models(thing)
