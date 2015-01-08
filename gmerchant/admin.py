from django.contrib import admin
from django.conf import settings
from models import GoogleMerchantAccount, APIServiceCredentials, GoogleCategory, GoogleProduct, GoogleProductDetails
from oscar.core.loading import get_model, get_class


Product = get_model("catalogue","Product")
ProductAdmin = get_class("catalogue.admin","ProductAdmin")

# First, un-register the Existing Product Admin

admin.site.unregister(Product)

class GoogleProductDetailsAdmin(admin.StackedInline):
    model = GoogleProductDetails
    extra = 0
    max_num = 1 #Lazy way to enforce Singleton-like behaviour.

    exclude = ("google_product",)

class GoogleExtendedProductAdmin(ProductAdmin):
    inlines = ProductAdmin.inlines + [GoogleProductDetailsAdmin,]

#Now we re-register the Product admin class
admin.site.register(Product, GoogleExtendedProductAdmin)

admin.site.register(GoogleMerchantAccount)
admin.site.register(APIServiceCredentials)
admin.site.register(GoogleCategory)

# This isn't necessary during normal operations
if settings.DEBUG:
    admin.site.register(GoogleProduct)

