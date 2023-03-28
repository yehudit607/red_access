from django.db import models
from api.models.company import Company


class Configuration(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='configurations')
    malicious_words = models.TextField()
    version = models.IntegerField(default=0)

    def __str__(self):
        return f"Configuration #{self.pk} for company {self.company.name}"
