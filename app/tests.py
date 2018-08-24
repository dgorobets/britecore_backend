from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import RiskType


class RiskTypeViewsTests(APITestCase):
    """A class used for testing risk type views.
    """

    def test_get_risk_types_list(self):
        RiskType.objects.bulk_create([
            RiskType(name='Life'),
            RiskType(name='Health'),
            RiskType(name='Property'),
            RiskType(name='Auto'),
            RiskType(name='Prize'),
        ])

        response = self.client.get(reverse('risktype-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), RiskType.objects.count())

    def test_get_risk_types_detail(self):
        risk_type, _ = RiskType.objects.get_or_create(name='Auto')

        response = self.client.get(reverse('risktype-detail', args=[risk_type.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], risk_type.id)
        self.assertEqual(response.data['name'], risk_type.name)
