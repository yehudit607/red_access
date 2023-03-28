from celery import shared_task
import requests
from rest_framework import status

from antivirus.antivirus import settings
from antivirus.redis import RedisWords

redis_words = RedisWords()

@shared_task
def fetch_configuration_data(version):
    response = requests.get(f"http://localhost/api/config?version={version}&company_id={settings.COMPANY_ID}")
    if response.status_code == status.HTTP_200_OK:
        data = response.json()
        if data.get('malicious_words'):
            redis_words.set_malicious_words(data['malicious_words'])
            redis_words.set_version(data['version'])
