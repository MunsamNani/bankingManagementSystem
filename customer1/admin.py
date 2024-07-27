from django.contrib import admin
from customer1.models import customer

class customer_Admin(admin.ModelAdmin):
    list_display=['branch_code','branch_name','customer_name','account_number','amount','date']

admin.site.register(customer,customer_Admin)


# Register your models here.
