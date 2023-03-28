#def get_session_logger():
from django.http import JsonResponse
import logging


def get_session_logger():
    return logging.getLogger("config")

def is_logged_in(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)

        return JsonResponse({"error": "wrong credentials"}, status=403)

    return wrapper


logger = get_session_logger()
