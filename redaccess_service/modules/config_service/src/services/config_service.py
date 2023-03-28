from api.models import Configuration
from modules.infra.base_service import BaseService, logger


class ConfigService(BaseService):
    model = Configuration

    @classmethod
    def get(cls, company_id: int, version: int = None):
        if company_id:
            conf = cls.model.objects.filter(company_id=company_id).first()
            print(conf)
            if conf:

                return conf if conf.version > version else False
            return None

    @classmethod
    def create(cls, config_data: dict) -> int:
        logger.debug(f"Creating a new config..")
        config = Configuration(
            company_id=config_data.get("company_id"),
            malicious_words=config_data.get("malicious_words"),
            version=config_data.get("version"),
        )
        config.save()
        logger.debug(f"Config successfully created with id: {config.id}.")
        return config.id

    @classmethod
    def update(cls, company_id: int, config_data: dict) -> bool:
        logger.debug(f"Updating config for company : {company_id}.")
        config = cls.model.objects.filter(company_id=company_id).first()
        if not config:
            logger.debug(f"Config with id {config.id} not found.")
            return False

        config.company_id = config_data.get("company_id", config.company_id)
        config.malicious_words = config_data.get("malicious_words", config.malicious_words)
        config.version += 1  # Increment the version by 1
        config.save()
        logger.debug(f"Config with id {config.id} updated successfully.")
        return config

    @classmethod
    def delete(cls, config_id: int) -> bool:
        logger.debug(f"Deleting config with id: {config_id}.")
        config = cls.model.objects.filter(id=config_id).first()
        if not config:
            logger.debug(f"Config with id {config_id} not found.")
            return False

        config.delete()
        logger.debug(f"Config with id {config_id} deleted successfully.")
        return True
