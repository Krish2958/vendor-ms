from rest_framework import routers

from .views import HistoricalPerformanceViewset, PurchaseOrderViewSet, VendorViewSet

router = routers.DefaultRouter()

# API
router.register(r"vendors", VendorViewSet, basename="vendor")
router.register(r"purchase_orders", PurchaseOrderViewSet, basename="purchase_orders")
router.register(r"performance", HistoricalPerformanceViewset, basename="performance")
urlpatterns = router.urls
