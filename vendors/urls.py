from rest_framework import routers

from .views import VendorViewSet

router = routers.DefaultRouter()

# API
router.register(r"vendors", VendorViewSet, basename="vendor")

urlpatterns = router.urls
