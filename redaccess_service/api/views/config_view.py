
from django.http import JsonResponse
from rest_framework.views import APIView
from http import HTTPStatus

from api.serializers.config_serializer import ConfigurationSerializer
from modules.config_service import ConfigSDK
config_sdk = ConfigSDK()


class ConfigView(APIView):
    def get(self, request):
        version = request.query_params.get("version")
        company_id = request.query_params.get("company_id")

        if not version or not company_id:
            return JsonResponse({"error": "version and company_id are required"}, status=HTTPStatus.BAD_REQUEST)

        malicious_words = self.retrieve(company_id, int(version))

        if not malicious_words:
            return JsonResponse({"error": "No configuration found for this version and company"}, status=HTTPStatus.NOT_FOUND)

        return JsonResponse(ConfigurationSerializer(malicious_words).data, status=HTTPStatus.OK)

    def retrieve(self, company_id, version):
        return config_sdk.config_service.get(company_id, version)

    def put(self, request):
        company_id = request.data.get("company_id")
        malicious_words = request.data.get("malicious_words")

        if not company_id or not malicious_words:
            return JsonResponse({"error": "company_id, and malicious_words are required"}, status=HTTPStatus.BAD_REQUEST)

        config = config_sdk.config_service.update(company_id, request.data)

        return JsonResponse(ConfigurationSerializer(config).data, status=HTTPStatus.OK)
