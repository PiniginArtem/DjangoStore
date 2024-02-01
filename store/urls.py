from django.urls import path
from rest_framework import routers
from .views import CurrentDateView, RandomView, HelloView, IndexView, ProductSingleView, CartView, ShopView, CartViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

app_name = 'store'

urlpatterns = [
   # ссылки для первой части практики
   path('welcome/', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()),
   path('random/', RandomView.as_view()),
   path('hello/', HelloView.as_view()),
   # ссылки для третьей части практики
   path('', ShopView.as_view(), name='shop'),
   path('cart/', CartView.as_view(), name='cart'),
   path('product/<int:id>', ProductSingleView.as_view(), name='product'),
]