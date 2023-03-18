










from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        username=input('Enter a username: ')
        email=input('Enter a email address: ')
        password=input('Enter a password: ')

        User.objects.create_superuser(username, email, password)

        self.stdout.write(self.style.SUCCESS('Superuser created succesfully!'))