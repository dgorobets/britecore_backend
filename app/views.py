from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import RiskTypeSerializer
from .models import RiskType


class RiskTypeViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    """A viewset class used for risk types API
    """
    queryset = RiskType.objects.prefetch_related('eav_values__attribute')
    serializer_class = RiskTypeSerializer
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        data = self.get_queryset().values('id', 'name')
        return Response(data)
