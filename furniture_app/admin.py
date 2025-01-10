from django.contrib import admin
from .models import Orders
from .models import Contact

# Register your models here.
admin.site.register(Orders)
admin.site.register(Contact)