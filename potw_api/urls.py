from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from potw_api.views import (
    places,
    sync_user,
)
urlpatterns = [
    path('api/places', places ),
    path('api/sync_user', sync_user),
    path('api/schema/', SpectacularAPIView.as_view(), name = 'schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name = 'schema')),
]