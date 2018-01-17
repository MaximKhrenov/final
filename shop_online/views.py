from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins
from shop_online.models import (Product, Category, User, Baskets)
from rest_framework.permissions import IsAuthenticated
from shop_online.serializers import (
    ProductSerializers,
    CategorySerializers,
    UserSerializers,
    BasketSerializers,
)


class ProductView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  # mixins.CreateModelMixin,
                  ):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class CategoryView(GenericViewSet,
                   mixins.ListModelMixin,
                   # mixins.CreateModelMixin,
                   ):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class UserView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               ):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class BasketView(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin, ):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializers
    queryset = Baskets.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
