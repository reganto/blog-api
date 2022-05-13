"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from dj_rest_auth.views import PasswordResetConfirmView

# def account_confirm_email(request, key):
#     return render(request, "api/account-confirm-email.html", {"key": key})

# account-confirm-email.html:
# <form action="/api/rest/auth/registration/verify-email/" method="post">
# <!-- url rest_verify_email -->
# {% csrf_token %}
# <input type="text" name="key" id="key" value="{{ key }}" hidden="hidden" />
# </form>


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path(
        "api/auth/registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path("api/auth/browable/", include("rest_framework.urls")),
    # path(
    #     "api/auth/registration/account-confirm-email/<str:key>/",
    #     account_confirm,
    #     name="account_confirm_email",
    # ),
    path(
        "api/auth/password-reset-confirm/<uid64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
