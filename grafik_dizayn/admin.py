from django.contrib import admin

from grafik_dizayn.models import Kurs


# Register your models here.
class KursModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description','price']
    list_display = ['title','price']


admin.site.register(Kurs)
