from django.core.management.base import BaseCommand, CommandError

from local_shop.gmerchant.models import GoogleMerchantAccount, GoogleProduct

from oscar.core.loading import get_class, get_model

Product = get_model("catalogue","Product")

class GMerchantMigrationError(CommandError):
    pass

class Command(BaseCommand):
    help = 'Migrates data from Product model to updated GoogleProduct Model'

    def handle(self, *args, **options):
        self.test_migration()
        self.migrate_data()
        print "Complete!"

    def test_migration(self):
        #Is Migration Necessary?
        p = Product()
        if hasattr(p,"google_shopping_description"):
            return True
        else:
            raise GMerchantMigrationError("You don't need to run this.")
        #Test whether or not we can do the migration.
        t = GoogleProduct()
        if hasattr(t,"google_product_updated"):
            return True
        else:
            raise GMerchantMigrationError("You need to migrate your gmerchant application first.")

    def migrate_data(self):

        gproducts = GoogleProduct.objects.all().select_related()
        for p in gproducts:
            try:
                p.google_shopping_description = p.product.google_shopping_description
                p.publish_google_shopping = p.product.publish_google_shopping
                p.google_taxonomy = p.product.google_taxonomy

                p.save()
            except:
                print "Couldn't migrate %s" % p.id

            else:
                print "Updated: %s" % p.id