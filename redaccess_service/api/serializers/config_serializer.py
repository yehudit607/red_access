from rest_framework import serializers

from api.models import Configuration
from api.serializers.company_serializer import CompanySerializer


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['company_id', 'malicious_words', 'version']