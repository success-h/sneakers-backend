
from django.urls import path
from .views import CartViewSet, ProductViewSet, CategoryViewSet, ProductImageViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category' )
router.register('product', ProductViewSet, basename='product')
router.register('productimage', ProductImageViewSet, basename='productimage')
router.register('cart', CartViewSet, basename='cart' )

urlpatterns = router.urls
