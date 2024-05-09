from datetime import timezone

from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def calculate_on_time_delivery_rate(self):
        completed_orders = self.purchaseorder_set.filter(status="completed")
        total_completed_orders = completed_orders.count()
        if total_completed_orders == 0:
            return 0.0
        on_time_orders = completed_orders.filter(
            delivery_date__lte=models.F("expected_delivery_date")
        )
        on_time_delivery_rate = (on_time_orders.count() / total_completed_orders) * 100
        return round(on_time_delivery_rate, 2)

    def calculate_quality_rating_avg(self):
        completed_orders = self.purchaseorder_set.filter(status="completed").exclude(
            quality_rating__isnull=True
        )
        if not completed_orders.exists():
            return None
        quality_rating_sum = completed_orders.aggregate(models.Sum("quality_rating"))[
            "quality_rating__sum"
        ]
        quality_rating_avg = quality_rating_sum / completed_orders.count()
        return round(quality_rating_avg, 2)

    def calculate_average_response_time(self):
        completed_orders = self.purchaseorder_set.filter(status="completed").exclude(
            acknowledgment_date__isnull=True
        )
        if not completed_orders.exists():
            return None
        response_times = [
            (po.acknowledgment_date - po.issue_date).total_seconds()
            for po in completed_orders
        ]
        average_response_time = sum(response_times) / len(response_times)
        return round(average_response_time / 3600, 2)  # Convert seconds to hours

    def calculate_fulfillment_rate(self):
        total_orders = self.purchaseorder_set.count()
        if total_orders == 0:
            return 0.0
        fulfilled_orders = self.purchaseorder_set.filter(
            status="completed", has_issues=False
        )
        fulfillment_rate = (fulfilled_orders.count() / total_orders) * 100
        return round(fulfillment_rate, 2)


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True)
    has_issues = models.BooleanField(default=False)

    def __str__(self):
        return self.po_number

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Trigger performance metric calculations when relevant events occur
        if self.status == "completed":
            self.vendor.calculate_on_time_delivery_rate()
            self.vendor.calculate_quality_rating_avg()
            self.vendor.calculate_average_response_time()
            self.vendor.calculate_fulfillment_rate()

    def acknowledge(self):
        self.acknowledgment_date = timezone.now()
        self.save()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
