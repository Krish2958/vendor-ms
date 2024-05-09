from django.contrib import admin
from django.urls import include, path
from drf_yasg.openapi import Info, License
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

documentation_schema_view = get_schema_view(
    Info(
        title=" VendorMS API",
        default_version="v1",
        description="This is the API engine for Vendor Managment System App.",
        license=License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("vendors.urls")),
    path(
        "documentation/",
        documentation_schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
