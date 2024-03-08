from django.core.management.base import BaseCommand
from base.models import NewsArticle
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete oldest items from NewsArticle if the total count exceeds a limit'

    def handle(self, *args, **options):
        # Define your limit
        limit = 50  # Adjust this according to your requirement

        # Get the total count of items
        total_count = NewsArticle.objects.count()

        if total_count > limit:
            # Calculate how many items to delete
            items_to_delete = total_count - limit

            # Query for the oldest items
            oldest_items = NewsArticle.objects.order_by('created')[:items_to_delete]

            # Delete the oldest items
            for item in oldest_items:
                item.delete()

            self.stdout.write(self.style.SUCCESS(f'Deleted {items_to_delete} oldest items from NewsArticle'))
        else:
            self.stdout.write(self.style.SUCCESS(
                f'Total count ({total_count}) is within the limit'))

