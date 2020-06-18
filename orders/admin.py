from django.contrib import admin
from .models import Flavor, Crust, Size, Extra, Pizza

admin.site.register(Flavor)
admin.site.register(Crust)
admin.site.register(Size)
admin.site.register(Extra)
admin.site.register(Pizza)