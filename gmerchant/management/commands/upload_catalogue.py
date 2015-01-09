from django.core.management.base import BaseCommand, CommandError

from local_shop.gmerchant.models import GoogleMerchantAccount

class GMAException(CommandError):
    pass

class Command(BaseCommand):
    help = 'Synchronizes Product Catalogue with Google Shopping.'

    def handle(self, *args, **options):
        self.sync_products()
        print "Complete!"

    def sync_products(self):
        self.gma = gma = GoogleMerchantAccount.objects.first()

        if not gma:
            raise GMAException("You must set up a Google Merchant Account in the admin first.")

        else:
            gma.init_client()
            gma.refresh_catalogue()