from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import HistoricalPerformance, PurchaseOrder, Vendor
from .serializers import (
    HistoricalPerformanceSerializer,
    PurchaseOrderSerializer,
    VendorSerializer,
)


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=["GET"], url_path="performance")
    def get_vendor_performance(self, request, pk=None):
        vendor = self.get_object()
        performance_metrics = {
            "on_time_delivery_rate": vendor.calculate_on_time_delivery_rate(),
            "quality_rating_avg": vendor.calculate_quality_rating_avg(),
            "average_response_time": vendor.calculate_average_response_time(),
            "fulfillment_rate": vendor.calculate_fulfillment_rate(),
        }
        return Response(performance_metrics)


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=["POST"], url_path="acknowledge")
    def acknowledge_purchase_order(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledge()
        return Response({"detail": "Purchase order acknowledged successfully"})


class HistoricalPerformanceViewset(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [AllowAny]
