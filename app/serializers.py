from eav.models import Value, Attribute, EnumGroup, EnumValue
from rest_framework import serializers
from django.forms import ALL_FIELDS

from .models import RiskType


class EnumValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnumValue
        fields = ALL_FIELDS


class EnumGroupSerializer(serializers.ModelSerializer):
    values = EnumValueSerializer(many=True, read_only=True)

    class Meta:
        model = EnumGroup
        fields = ALL_FIELDS


class AttributeSerializer(serializers.ModelSerializer):
    enum_group = EnumGroupSerializer()

    class Meta:
        model = Attribute
        fields = ALL_FIELDS


class ValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = Value
        fields = ALL_FIELDS


class RiskTypeSerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField()

    class Meta:
        model = RiskType
        fields = ('id', 'name', 'values')

    def get_values(self, obj):
        return ValueSerializer(obj.eav_values.all(), many=True, read_only=True).data
