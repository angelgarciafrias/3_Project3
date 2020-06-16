from django.contrib import admin
from .models import Flavors, Crusts, Sizes, Extras, Pizzas

class ExtraInline(admin.StackedInline):
    model = Extras.pizzas_extra.through
    extra = 1

class PizzasAdmin(admin.ModelAdmin):
    inlines = [ExtraInline]

class ExtrasAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizzas_extra",)

admin.site.register(Flavors)
admin.site.register(Crusts)
admin.site.register(Sizes)
admin.site.register(Extras, ExtrasAdmin)
admin.site.register(Pizzas, PizzasAdmin)