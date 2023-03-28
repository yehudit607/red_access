from django.views.decorators.csrf import csrf_exempt
from .tasks import MALICIOUS_WORDS

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser


async def is_malicious(line):
    line_content = line.decode('utf-8')
    for word in MALICIOUS_WORDS:
        if word in line_content:
            return True
    return False


@csrf_exempt
@api_view(["POST"])
@parser_classes([MultiPartParser])
async def scan_file_view(request):
    file = request.FILES.get('file')
    if not file:
        return JsonResponse({"error": "No file provided"}, status=400)

    # Read the file line by line asynchronously
    async for line in file:
        if await is_malicious(line):
            return JsonResponse({"result": "detected"})

    return JsonResponse({"result": "clean"})
