from django.contrib import admin
from .models import Post, Inventory, Order


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['item', 'item_quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_item', 'name', 'quantity', 'order_placed']


admin.site.register(Post)
admin.site.register(Order,OrderAdmin)
admin.site.register(Inventory,InventoryAdmin)
