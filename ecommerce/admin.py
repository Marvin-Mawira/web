from django.contrib import admin

# Register your models here.

from .models import ContactMessage
from .models import Product
from .models import product_detail


admin.site.register(ContactMessage)
admin.site.register(Product)
admin.site.register(product_detail)
