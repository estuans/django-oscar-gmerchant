
import requests

from django.core.management.base import BaseCommand, CommandError

from local_shop.gmerchant.models import GoogleMerchantAccount

class Command(BaseCommand):
    help = 'Synchronizes Inventory with Google Shopping.'

    def handle(self, *args, **options):
        self.sync_inventory()
        print "Complete!"

    def sync_inventory(self):
        self.gma = gma = GoogleMerchantAccount.objects.first()
        gma.init_client()
        gma.update_inventory()