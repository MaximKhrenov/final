from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from shop_online.views import (ProductView, CategoryView, UserView, BasketView, )

router = DefaultRouter()
router.register(r'product', ProductView)
router.register(r'category', CategoryView)
router.register(r'user', UserView)
router.register(r'basket', BasketView)
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]
