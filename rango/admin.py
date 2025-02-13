from django.contrib import admin
from rango.models import Category, Page, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

admin.site.register(Page)
# Register your models here.
...
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)