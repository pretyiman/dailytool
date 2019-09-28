from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blog.models import Expenses, Income, Contacts,catagory,subcatagory,warehouse,rack,item
# Register your models here.
admin.site.register(Expenses)
admin.site.register(Income)
admin.site.register(Contacts)
admin.site.register(catagory)
admin.site.register(subcatagory)
admin.site.register(warehouse)
admin.site.register(rack)
admin.site.register(item)
