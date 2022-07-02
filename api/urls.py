from django.urls import path

from api.views.health_check import HealthCheckView

urlpatterns = [
    path('health_check', HealthCheckView.as_view()),
]
