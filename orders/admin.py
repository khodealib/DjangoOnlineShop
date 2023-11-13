from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)
