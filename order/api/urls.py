from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order', views.OrderViewSet, basename='order')

urlpatterns = router.urls
