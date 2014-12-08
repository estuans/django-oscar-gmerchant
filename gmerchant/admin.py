from django.contrib import admin

from models import GoogleMerchantAccount, APIServiceCredentials, GoogleCategory, GoogleProduct

admin.site.register(GoogleMerchantAccount)
admin.site.register(APIServiceCredentials)
admin.site.register(GoogleCategory)
admin.site.register(GoogleProduct)