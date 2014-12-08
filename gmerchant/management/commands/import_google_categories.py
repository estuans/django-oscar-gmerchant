
import requests

from django.core.management.base import BaseCommand, CommandError

from local_shop.gmerchant.models import GoogleCategory

CATEGORY_SOURCE = "http://www.google.com/basepages/producttype/taxonomy.en-US.txt"


class Command(BaseCommand):
    help = 'Fetches the google product category list and stores them in the DB'


    def handle(self, *args, **options):

        req = requests.get(CATEGORY_SOURCE)
        raw_categories = req.text

        #import pdb; pdb.set_trace()

        self.build_categories(raw_categories)


    def build_categories(self,raw):
        cat_list = raw.split("\n")
        cat_list.pop(0) # Drop the comment in the header.

        for idx,val in enumerate(cat_list):
            cat, created = GoogleCategory.objects.get_or_create(source_idx=idx,name=val)
            if created:
                cat.save()



