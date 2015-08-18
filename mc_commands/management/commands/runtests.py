from django.core.management.base import BaseCommand
from django.conf import settings

from mc_commands.management.commands.helpers._test import test


class Command(BaseCommand):
    help = 'Runs the Test Suite with Coverage.'

    def handle(self, *args, **options):
        self.stdout.write('Starting Testss')
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        test(directory)
