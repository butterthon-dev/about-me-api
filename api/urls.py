from django.urls import path

from api.views.health_check import HealthCheckView

urlpatterns = [
    path('', HealthCheckView.as_view()),
]
