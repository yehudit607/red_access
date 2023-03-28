from .src.services.config_service import ConfigService


class ConfigSDK:
    def __init__(self) -> None:
        self.config_service = ConfigService()

