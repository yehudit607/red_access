from celery import shared_task
import requests

from antivirus.antivirus import settings

MALICIOUS_WORDS = []


@shared_task
def fetch_configuration_data(version):
    response = requests.get(f"http://localhost/api/config?version={version}&company_id={settings.COMPANY_ID}")
    if response.status_code == 200:
        data = response.json()
        if data.get('malicious_words'):
            global MALICIOUS_WORDS
            MALICIOUS_WORDS = data['malicious_words']
