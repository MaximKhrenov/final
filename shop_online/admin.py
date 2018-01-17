from django.contrib import admin
from django import forms
from shop_online.models import (Product, Category, )


class ProductsAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('create_pr', 'update_pr')


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('title_product', 'create_pr', 'update_pr')
    readonly_fields = ('create_pr', 'update_pr')


# class CatAdmin(admin.ModelAdmin):
#     list_display = ('title_category','created_product','update_product')
#

admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, )

# Register your models here.
