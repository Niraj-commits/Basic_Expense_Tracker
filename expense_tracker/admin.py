from django.contrib import admin
from .models import *

@admin.register(account)
# Register your models here.
class admin_panel(admin.ModelAdmin):
    list_display = ['id','name','description','amount','type']
    search_fields = []
    list_per_page = 10
    list_filter = ['type']
    search_fields = ['name','description','type']
    list_display_links = ['id']
    list_editable = ['name',"type"]