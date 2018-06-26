from django.contrib import admin
from .models import Rates_all


# Register your models here.

class AdminRates(admin.ModelAdmin):
    list_display = [field.name for field in Rates_all._meta.fields]

    class Meta:
        model = Rates_all

admin.site.register(Rates_all, AdminRates)
