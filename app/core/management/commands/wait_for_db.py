"""
Django Command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as PsycopgError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for the database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        while True:
            try:
                self.check(databases=["default"])
                break  # Exit loop when database is available
            except (PsycopgError, OperationalError) as e:
                self.stdout.write(f"Database unavailable, waiting 1 second... Error: {e}")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
