from django.core.management.base import BaseCommand, CommandError


# to run this file "python manage.py test_command <pass argument if u want>" and
# first its add_argument and then handle method will be called
# if we pass argument so first in add_arguments we set using parser.add_argument('poll_ids', type=int) and
# we use passed argument in option dictionary in handle method
class Command(BaseCommand):
    help = 'Test Redis Cache Connection'

    def add_arguments(self, parser):
        # pass
        parser.add_argument('poll_ids', type=int)

    def handle(self, *args, **kwargs):
        print(kwargs['poll_ids'])
        self.stdout.write(self.style.SUCCESS('success...'))
