from django.contrib import admin

from .models import Product, Image, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image)
