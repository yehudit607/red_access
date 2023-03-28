from rest_framework import serializers


class CompanySchema(serializers.Serializer):
    name=serializers.CharField()