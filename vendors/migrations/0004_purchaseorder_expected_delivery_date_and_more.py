# Generated by Django 5.0.4 on 2024-05-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_historicalperformance'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='expected_delivery_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='has_issues',
            field=models.BooleanField(default=False),
        ),
    ]