django-oscar-gmerchant
======================

Integration with Google Merchant Center and Django Oscar

THIS IS STILL AS WORK IN PROGRESS.

It should however be fairly straight forward to use.
Simply add to your post-oscar applications list and you should be on your way.

If you receive warnings about the ProductAdminClass, then you should look at changing
the ProductAdmin that is being modified inside of gmerchant/admin to point directly at
your-likely-to-have-been modified class.


USAGE
=====

1. Install.
2. Run import_google_categories.
3. Add a Google Merchant account to your admin.
4. Add Google Merchant Records to the products you wish publish.
5. Run upload_catalogue using a cronjob.

Contributions welcome.


IDEAS / TBD
===========

* Add post-save signals to Product model save to trigger updates to single product records.
* Complete integration with "Store Inventory Managment".
* Add Oscar Dashboard integration.
* Improve Merchant account handling.

