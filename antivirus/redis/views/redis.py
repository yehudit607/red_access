from rest_framework.decorators import api_view
from django.http import JsonResponse

from .. import RedisWords


@api_view(["GET"])
def health_check(request):
    try:
        return JsonResponse(
            {"status": "UP" if RedisWords().ping() else "DOWN"},
            status=200,
        )
    except:
        return JsonResponse({"status": "DOWN"}, status=403)
