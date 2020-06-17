from django.contrib import admin
from .models import Flavor, Crust, Size, Extra, Pizza

class ExtraInline(admin.StackedInline):
    model = Extra.pizzas_extra.through
    extra = 1

class PizzaAdmin(admin.ModelAdmin):
    inlines = [ExtraInline]

class ExtraAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizzas_extra",)

admin.site.register(Flavor)
admin.site.register(Crust)
admin.site.register(Size)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Pizza, PizzaAdmin)