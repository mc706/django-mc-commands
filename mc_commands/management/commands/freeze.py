from django.core.management.base import BaseCommand
from mc_commands.management.commands.helpers._freeze import freeze


class Command(BaseCommand):
    help = 'Shortcut to freeze package details to requirements.txt'

    def handle(self, *args, **options):
        self.stdout.write('Freezing Requirements...')
        freeze()


