
from django.urls import path
from .views import ProductViewSet, CategoryViewSet, ProductImageViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category' )
router.register('product', ProductViewSet, basename='product')
router.register('productimage', ProductImageViewSet, basename='productimage')


urlpatterns = router.urls
