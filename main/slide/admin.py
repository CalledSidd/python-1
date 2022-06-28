from django.contrib import admin
from . models import Pro


class ProAdmin(admin.ModelAdmin):
    list_display = ('name','price')
# Register your models here.
admin.site.register(Pro,ProAdmin)