from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("v1/", include("api.v1.urls")),
    path("v2/", include("api.v2.urls")),
    path("v3/", include("api.v3.urls")),
    path("v4/", include("api.v4.urls")),
]
