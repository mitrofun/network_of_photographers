# Generated by Django 3.0.8 on 2020-07-24 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Thing',
                'verbose_name_plural': 'Things',
                'db_table': 'things',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ThingInUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='things_in_use', to='things.Thing', verbose_name='Thing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='things_in_use', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Thing in use',
                'verbose_name_plural': 'Things in use',
                'db_table': 'things_in_use',
            },
        ),
        migrations.CreateModel(
            name='ThingInCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='things_in_city', to='geo.City', verbose_name='City')),
                ('thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='things_in_city', to='things.Thing', verbose_name='Thing')),
            ],
            options={
                'verbose_name': 'Things in city',
                'verbose_name_plural': 'Things in cities',
                'db_table': 'things_in_cities',
            },
        ),
    ]
