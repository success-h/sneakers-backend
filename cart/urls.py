from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'cart'
router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart' )

urlpatterns = router.urls