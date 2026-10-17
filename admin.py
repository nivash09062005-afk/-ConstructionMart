from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "unit", "stock", "supplier_name")
    list_filter = ("category",)
    search_fields = ("name", "supplier_name")

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "quantity", "unit_price")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "phone", "payment_method", "total", "status", "created_at")
    list_filter = ("payment_method", "status", "created_at")
    search_fields = ("customer_name", "email", "phone")
    inlines = [OrderItemInline]
