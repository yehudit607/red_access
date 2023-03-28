from rest_framework import serializers

from api.schemas.company_scheam import CompanySchema


class ConfigSchema(serializers.Serializer):
    company = CompanySchema(required=True)
    malicious_words = serializers.CharField()
    version = serializers.IntegerField(required=True, default=0)
