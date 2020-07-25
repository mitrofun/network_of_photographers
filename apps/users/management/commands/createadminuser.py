from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create admin user'
    first_name = 'Mike'
    last_name = 'Wazowski'
    username = 'admin'
    email = 'admin@a.ru'
    password = 'admin'

    def handle(self, *args, **options):
        try:
            get_user_model().objects.get(username=self.username)
            message = f'[{__name__}] Admin already exists.'
            self.stdout.write(self.style.SUCCESS(message))
        except get_user_model().DoesNotExist:
            admin = get_user_model().objects.create(
                first_name=self.first_name,
                last_name=self.last_name,
                username=self.username,
                email=self.email,
                is_superuser=True,
                is_staff=True,
                is_active=True,
            )
            admin.set_password(self.password)
            admin.save()
            message = f'[{__name__}] Admin successfully created.'
            self.stdout.write(self.style.SUCCESS(message))
