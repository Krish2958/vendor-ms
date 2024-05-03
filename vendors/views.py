from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Vendor
from .serializers import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST"], url_path="")
    def create_vendor(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["GET"], url_path="")
    def list_vendors(self, request):
        vendors = self.queryset
        serializer = self.serializer_class(vendors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path="")
    def retrieve_vendor(self, request, pk=None):
        vendor = self.get_object()
        serializer = self.serializer_class(vendor)
        return Response(serializer.data)

    @action(detail=True, methods=["PUT"], url_path="")
    def update_vendor(self, request, pk=None):
        vendor = self.get_object()
        serializer = self.serializer_class(vendor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=["DELETE"], url_path="")
    def delete_vendor(self, request, pk=None):
        vendor = self.get_object()
        message = f"Vendor is deleted"
        vendor.delete()
        return Response({"message": message})
