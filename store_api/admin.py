from django.contrib import admin
from store_api.models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
