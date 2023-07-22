from django.urls import path, include
from potw_api.views import (
    PlaceListApiView,
)

urlpatterns = [
    path('api', PlaceListApiView.as_view()),
]