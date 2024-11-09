from django.core.management.base import BaseCommand
from tailapp.consumers import run_watcher


class Command(BaseCommand):
    def handle(self, *args, **options):
        run_watcher()
