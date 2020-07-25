import pytest
from django.contrib.contenttypes.models import ContentType
from mixer.backend.django import mixer as _mixer


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def user(mixer, city):
    return mixer.blend(
        'users.user',
        city=city,
        username='vv_first',
        first_name='Vovcik',
        last_name='First',
    )


@pytest.fixture
def second_user(mixer, city):
    return mixer.blend(
        'users.user',
        city=city,
        username='dv_second',
        first_name='Dimas',
        last_name='Second',
    )


@pytest.fixture
def country(mixer):
    return mixer.blend('geo.country', name='Russia')


@pytest.fixture
def city(mixer, country):
    return mixer.blend('geo.city', country=country, name='Tcargrad')


@pytest.fixture
def thing(mixer, city, user):
    thing = mixer.blend('things.thing', name='Throne')
    mixer.blend('things.thingincity', thing=thing, city=city)
    mixer.blend('things.thinginuse', thing=thing, user=user)
    return thing


@pytest.fixture
def second_thing(mixer, city, user):
    thing = mixer.blend('things.thing', name='NOT Round Table')
    mixer.blend('things.thingincity', thing=thing, city=city)
    mixer.blend('things.thinginuse', thing=thing, user=user)
    return thing


@pytest.fixture
def photo_country(mixer, country):
    return mixer.blend(
        'gallery.photo',
        name='Russia photo',
        content_type=ContentType.objects.get(model='country'),
        object_id=country.id,
        is_approved=True,
    )


@pytest.fixture
def photo_city(mixer, city):
    return mixer.blend(
        'gallery.photo',
        name='Tcargrad photo',
        location=city,
        content_type=ContentType.objects.get(model='city'),
        object_id=city.id,
        is_approved=True,
    )


@pytest.fixture
def photo_thing(mixer, thing, city):
    return mixer.blend(
        'gallery.photo',
        name='Game of Throne',
        location=city,
        content_type=ContentType.objects.get(model='thing'),
        object_id=thing.id,
        is_approved=True,
    )


@pytest.fixture
def photo_user(mixer, user, city):
    return mixer.blend(
        'gallery.photo',
        location=city,
        content_type=ContentType.objects.get(model='user'),
        object_id=user.id,
        is_approved=True,
    )


@pytest.fixture
def second_photo_thing(mixer, second_thing):
    return mixer.blend(
        'gallery.Photo',
        name='On table',
        content_type=ContentType.objects.get(model='thing'),
        object_id=second_thing.id,
        is_approved=True,
    )
