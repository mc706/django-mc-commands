from django.core.management.base import BaseCommand
from django.conf import settings

from mc_commands.management.commands.helpers._cut import cut


class Command(BaseCommand):
    help = 'Cut a release. Updates Change log, increments version, and creates tag.'

    def handle(self, *args, **options):
        self.stdout.write('Cutting Release...')
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        cut(directory, args)
