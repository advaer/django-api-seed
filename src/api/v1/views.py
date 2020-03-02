from rest_framework import status
from rest_framework.response import Response

from src.api.core.views import BaseAPIView


class HealthView(BaseAPIView):

    def get(self, request):
        return Response(
            {'message': 'It works!'},
            status=status.HTTP_200_OK
        )
