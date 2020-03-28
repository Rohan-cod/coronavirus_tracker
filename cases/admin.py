from django.contrib import admin

# Register your models here.

from .models import Data

class DataAdmin(admin.ModelAdmin):
    class Meta:
	    model = Data

admin.site.register(Data,DataAdmin)