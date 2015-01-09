from django.contrib.sites.models import Site

MAX_PAGE_SIZE = 50
BATCH_SIZE = 50
BRAND = "Example Brand"
PREFIX = "example#"
PROTOCOL = "http://"
try:
    SITE = Site.objects.first().domain
except:
    SITE = "www.example.com"
SITE_ROOT = PROTOCOL + SITE