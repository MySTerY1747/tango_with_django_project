from django.contrib import admin
from rango.models import Category, Page


#  Customizing fields and order
class PageAdmin(admin.ModelAdmin):
    fields = ["title", "category", "url"]
    list_display = ("title", "category", "url")


# Register your models here.

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
