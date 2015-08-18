from django.core.management.base import BaseCommand
from django.conf import settings

from mc_commands.management.commands.helpers._bootstrap import bootstrap


class Command(BaseCommand):
    help = 'Sets up settings files and other files to be used by other commands'

    def handle(self, *args, **options):
        self.stdout.write('Bootstrapping...')
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        bootstrap(directory)


