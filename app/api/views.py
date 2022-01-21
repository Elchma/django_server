from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Coordinate
from .serializers import CoordinateSerializer

class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
             {"Success": "Coordinate added successfully"},
             status=status.HTTP_201_CREATED,
             headers=headers)