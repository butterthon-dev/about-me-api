from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from api.enums import HttpMethods


class HealthCheckView(APIView):
    @extend_schema(
        methods=[HttpMethods.GET],
        description='ヘルスチェックAPI',
        responses={200: OpenApiTypes.STR},)
    def get(self, request, *args, **kwargs):
        return Response('Healthy')
