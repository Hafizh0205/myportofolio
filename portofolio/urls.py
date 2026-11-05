from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/projects/', permanent=True)),
    path('projects/', include('main.urls')),
    path('contacts/', include('contacts.urls')),
    path("api/v1/", include("main.api_urls")),
    path("api-auth/", include("rest_framework.urls")),
]