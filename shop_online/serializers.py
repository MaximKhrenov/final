from rest_framework import serializers
from shop_online.models import (Product, Category, User, Baskets)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )

        def create_user(self, validate_date):
            user = User(
                email=validate_date['email'],
                username=validate_date['username'],
                first_name=validate_date['first_name'],
                last_name=validate_date['last_name'],
            )

            user.set_password(validate_date['password'])
            user.save()

            return user


class BasketSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    count_products = serializers.IntegerField(write_only=True)
    price_product = serializers.IntegerField(read_only=True)

    class Meta:
        model = Baskets
        exclude = ()
        fields = ('user', 'title','count_products','price_product', )

    def create(self, validated_data):
        user = validated_data['user']
        count_products = validated_data['count_products']
        title = validated_data['title']
        price = Product.objects.get(title_product=title)
        basket = Baskets(
            user=user,
            title=title,
            price_product=price.price_product * count_products,
            count_products=count_products,

        )
        basket.save()
        return basket
