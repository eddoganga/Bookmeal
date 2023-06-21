from django.contrib import admin
from .models import Category, RegularPizza, SicilianPizza, Toppings, Sub, Pasta, Salad, Rice, UserOrder, SavedCarts
from tinymce import tinymce
from django.db import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': tinymce()},
            }

class RegularPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': tinymce()},
            }

class SicilianPizzaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': tinymce()},
            }


admin.site.register(Category,CategoryAdmin)
admin.site.register(RegularPizza, RegularPizzaAdmin)
admin.site.register(SicilianPizza, SicilianPizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Rice)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)